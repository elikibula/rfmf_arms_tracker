from django.contrib import admin
from django.urls import path, include


# Admin Site Config
admin.site.site_header = 'RFMF Arms Tracker Sample'
admin.site.site_title = 'RFMF Arms Tracker Sample'
admin.site.index_title = 'RFMF Arms Tracker Web Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('tracker.urls')),
]
