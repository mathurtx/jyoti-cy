"""jyoti_content_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from repository.views import JyotiContentService
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Jyoti Content Service API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/content/schema/', schema_view),
    url(r'^api/content/create/report', JyotiContentService.as_view({'post': 'create_report'})),
    url(r'^api/content/report/(?P<id>[0-9]+)', JyotiContentService.as_view({'get': 'get_report_by_id'})),
    url('r^api/content/report/(?P<reportType>\w+)', JyotiContentService.as_view({'get':'get_reports_by_report_type'})),
    url('r^api/content/create/bulk/reports', JyotiContentService.as_view({'post':'create_bulk_reports'})),
    url('r^api/content/report/(?P<reportType>\w+)/count/city', JyotiContentService.as_view({'get': 'get_report_count_type_by_city'})),
    url('r^api/content/report/(?P<city>\w+)/count',JyotiContentService.as_view({'get': 'get_report_count_by_city'})),
    url('r^api/content/report/location', JyotiContentService.as_view({'post': 'get_reports_by_location'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
