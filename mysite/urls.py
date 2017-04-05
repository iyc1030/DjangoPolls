from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include("pollsapp.urls")),
    url(r'^polls/', include("pollsapp.urls", namespace="pollsapp")),
]
