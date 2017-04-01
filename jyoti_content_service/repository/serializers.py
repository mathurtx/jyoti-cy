from rest_framework import serializers
from .models import ReportTable, LocationFactTable


class ReportTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportTable
        fields = '__all__'


class LocationFactTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationFactTable
        fields = '__all__'