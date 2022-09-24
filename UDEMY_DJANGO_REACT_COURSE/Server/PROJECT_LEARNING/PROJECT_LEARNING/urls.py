from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app1/",include('APP_LEARNING.urls'))
    
]




## this two lines are for generating static files 
## url pattern
urlpatterns += staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

