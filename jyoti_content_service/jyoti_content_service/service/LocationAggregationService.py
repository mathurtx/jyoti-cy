from repository.models import *
from django.db.models import Count
from geopy.distance import *
import json


class LocationAggregationService:

    def generate_report_type_by_count(self):
        aggregate_results = ReportTable.objects.values('city', 'report_type').annotate(report_type_count=Count("report_type"))
        for result in aggregate_results:
            payload = LocationFactTable(latitude=result.latitude, longitude=result.longitude, report_type=result.report_type, report_type_count=result.report_type_count)
            payload.save()


    def generate_report_type_count_by_city(self):
        aggregate_results = ReportTable.objects.values('city').annotate(report_count=Count('city'))
        for result in aggregate_results:
            payload = ReportCountFactTable(city=result.city, report_count=result.report_count)
            payload.save()

