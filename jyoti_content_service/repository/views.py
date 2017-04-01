from rest_framework import viewsets
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import ReportTableSerializer, LocationFactTableSerializer
from .models import ReportTable, LocationFactTable
from geopy.distance import great_circle
from multiprocessing import Pool


class JyotiContentService(viewsets.ViewSet):

    RADIUS = 5

    def create_report(self, request):
        serializer = ReportTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_report_by_id(self, request, id):
        report = ReportTable.objects.get(id=id)
        serializer = ReportTableSerializer(report, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_report_type_count_by_location(self, request, ids):
        pass

    def get_reports_by_report_type(self, request, reportType):
        reports = ReportTable.objects.get(report_type=reportType)
        serializer = ReportTableSerializer(reports, data=request.data, many=True)
        if serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_report_by_location(self, request, latitude, longitude):
        reports = ReportTable.objects.all()
        serializer = ReportTableSerializer(reports, data=request.data, many=True)
        if serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_distance_between_points(self, source, destination):
        if great_circle(source, destination).miles <= self.RADIUS:
            return great_circle(source, destination).miles
        else:
            return None
