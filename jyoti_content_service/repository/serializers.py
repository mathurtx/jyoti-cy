from rest_framework import serializers
from .models import *


class ReportTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportTable
        fields = '__all__'


class LocationFactTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationFactTable
        fields = '__all__'

class ReportCountFactTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportCountFactTable
        fields = '__all__'