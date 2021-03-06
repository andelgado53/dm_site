from django.conf.urls import patterns, include, url
#from reporting import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dmsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^reporting/$', 'reporting.views.index',{'template': 'main.html'}, name = 'main'),
    url(r'^reporting/login/$', 'reporting.views.log_in', name = 'log_in'),
    url(r'^reporting/register/$', 'reporting.views.register', name = 'register'),
    url(r'^reporting/logout/$', 'reporting.views.log_out', name='log_out'),
    url(r'reporting/twitt_stream/$', 'reporting.views.twit_stream', {'template': 'twit.html'}, name = 'twit_stream'),
    url(r'^reporting/(?P<category>\w+)/$', 'reporting.views.report_request', {'template': 'report.html'}, name = 'report_request'),
    url(r'^reporting/[a-z]+_?[a-z]+/results/$', 'reporting.views.display_results', {'template': 'results.html'}, name = 'display_results'),

    
)
