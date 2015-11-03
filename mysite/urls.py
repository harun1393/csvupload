from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'service.views.login_view', name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^service/', include('service.urls')),
    url(r'^login/$', 'service.views.login_view', name='login'),
)
