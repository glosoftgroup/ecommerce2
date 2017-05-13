
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    #django admin url
    url(r'^admin/', include(admin.site.urls)),
    #django rest framework url
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^category/$', views.category, name='category'),
    url(r'^record/$', views.records, name='records'),
]
