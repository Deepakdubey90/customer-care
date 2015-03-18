from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from city.models import City

class IndexView(TemplateView):
    template_name = 'customrcare/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        return self.render_to_response(context)
