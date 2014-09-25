from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ljsweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', TemplateView.as_view(template_name="main/test.html")),
)
