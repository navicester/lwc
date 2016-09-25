from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home$', 'lwc.views.home', name='home'),
    url(r'^$', 'joins.views.home', name='home'),

    # url(r'^lwc/', include('lwc.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/*', include(admin.site.urls)), #add this *, otherwise, /admin will go to below next urlPattern, * means repeating precious char (0~n) 

    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
)

# handler404 = 'joins.views.server_error'
# handler403 = 'joins.views.server_error'
# handler500 = 'joins.views.server_error'