from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/",include('APP_LEARNING.urls')),
    path("auth/",obtain_auth_token)
    
]




## this two lines are for generating static files 
## url pattern
urlpatterns += staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

