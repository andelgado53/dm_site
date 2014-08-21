from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dmsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #(r'^', include('reporting.urls')),
    url(r'^reporting/$', 'reporting.views.index'),
    url(r'^reporting/(?P<category>\w+)/$', 'reporting.views.report_request'),
    url(r'^reporting/results/robin$', 'reporting.views.display_results'),
)
