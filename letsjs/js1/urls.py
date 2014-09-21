from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from js1.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'letsjs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'js1.views.home'),

    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    (r'^portal/', 'js1.views.portal_main_page'),

     # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),

    
)
