from django.conf.urls import url,include
from django.contrib import admin
from ide import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include("ide.urls")),
]
