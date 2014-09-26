from django.conf.urls import patterns, include, url
from mongo_app import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^insert_blog$', views.index, name='home'),
    # Examples:
    # url(r'^$', 'mongodb.views.home', name='home'),
    # url(r'^mongodb/', include('mongodb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
