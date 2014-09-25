from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ljsweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', TemplateView.as_view(template_name="main/index.html")),
    url(r'^home/$', views.loggedin, name='loggedin'),
    url(r'^signup/$', TemplateView.as_view(template_name="main/signup.html")),
    url(r'^login/$', views.auth_and_login, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.sign_up_in, name='register'),
)
