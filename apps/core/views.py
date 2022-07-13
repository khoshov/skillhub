from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MainPageConfig


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        config = MainPageConfig.get_solo()
        data['config'] = config
        data['meta'] = config.as_meta(self.request)
        return data


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def server_error(request):
    return render(request, '500.html', status=500)
