from django.conf.urls import patterns, include, url
#from reporting import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dmsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'reporting.views.index'),
    url(r'^(?P<report>\w+)/$', 'reporting.views.report_request'),
    
)
