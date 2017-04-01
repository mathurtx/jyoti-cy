from rest_framework import viewsets
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import *
from .models import *
from local_properties import *
from geopy.geocoders import Nominatim
from jyoti_content_service.service.LoadTwitterFeedService import LoadTwitterFeedService
import json

class JyotiContentService(viewsets.ViewSet):

    twitter_feed_service = LoadTwitterFeedService()
    geolocator = Nominatim()

    def create_report(self, request):
        try:
            latitude = request.data['latitude']
            longitude = request.data['longitude']
            location = self.geolocator.reverse(latitude, longitude)
            location_json = json.dumps(location.raw)
            location_json = json.loads(location_json)
            request.data['city'] = location_json['address']['city']
            serializer = ReportTableSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            Response(status=status.HTTP_400_BAD_REQUEST)

    def get_report_count_type_by_city(self, request, reportType):
        try:
            reports = LocationFactTable.objects.get(report_type=reportType)
            serializer = LocationFactTableSerializer(reports, many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            Response(status=status.HTTP_404_NOT_FOUND)

    def get_report_count_by_city(self, request, city):
        try:
            reports = ReportCountFactTable.objects.get(city=city)
            serializer = ReportCountFactTableSerializer(reports, many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            Response(status=status.HTTP_404_NOT_FOUND)

    def get_report_by_id(self, request, id):
        report = ReportTable.objects.get(id=id)
        serializer = ReportTableSerializer(report)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_reports_by_location(self, request):
        latitude = request.data['latitude']
        longitude = request.data['longittude']
        sql = FIND_ROWS_IN_RADIUS.format(source_latitude=latitude, source_longitude=longitude, radius=RADIUS)
        reports = ReportTable.objects.raw(sql)
        serializer = ReportTableSerializer(reports, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_reports_by_report_type(self, request, reportType):
        reports = ReportTable.objects.get(report_type=reportType)
        serializer = ReportTableSerializer(reports, many=True)
        if serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def create_bulk_reports(self, request):
        try:
            self.twitter_feed_service.load_file()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_417_EXPECTATION_FAILED)
