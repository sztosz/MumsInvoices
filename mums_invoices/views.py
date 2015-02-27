from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie


class LandingView(TemplateView):

    template_name = 'mums_invoices/landing.jade'
    success_url = 'mums_invoices:landing'

class IndexView(TemplateView):
    template_name = 'index.jade'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
