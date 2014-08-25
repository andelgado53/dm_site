from django.conf.urls import patterns, include, url
#from reporting import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dmsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^reporting/$', 'reporting.views.index'),
    url(r'reporting/twitt_stream/$', 'reporting.views.twit_stream'),
    url(r'^reporting/(?P<category>\w+)/$', 'reporting.views.report_request'),
    url(r'^reporting/[a-z]+_?[a-z]+/results/$', 'reporting.views.display_results'),
    
)
