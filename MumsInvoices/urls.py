from django.conf.urls import patterns, include, url
from django.contrib import admin

from MumsInvoices import views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'MumsInvoices.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url('^.*$', views.IndexView.as_view(), name='index'),

    # url(r'^$', views.LandingView.as_view(), name='landing'),
)
