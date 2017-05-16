
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
    url(r'^category_id/$', views.category_byId, name='category_byId'),
    url(r'^products/$', views.products, name='products'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'),

    url(r'^cart_add/$', views.add_to_cart, name='add_to_cart'),
]
