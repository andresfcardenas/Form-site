from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_example.views.home', name='home'),
    # url(r'^app_example/', include('app_example.foo.urls')),
    url(r'^form/', include('form.urls')),
    url(r'^$', 'app_example.views.home', name='home'),
    url(r'^list/$', 'app_example.views.list', name='list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
