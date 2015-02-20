from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework_nested import routers

from mums_invoices import views as main_views
from authentication import views as auth_views


router = routers.SimpleRouter()
router.register(r'accounts', auth_views.AccountViewSet)

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'MumsInvoices.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/', include(router.urls)),

    url('^.*$', main_views.IndexView.as_view(), name='index'),

    # url(r'^$', views.LandingView.as_view(), name='landing'),
)
