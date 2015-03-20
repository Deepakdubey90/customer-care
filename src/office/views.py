import json
from django.db import models
from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.views.generic import View, ListView
from django.db.models import Q
from organization.models import Organization
from state.models import State
from office.models import Office
from country.models import Country
from .forms import OfficeSearchForm
from city.models import City
from django import forms


class OfficeSearchView(ListView):

    def get(self, request, *args):
        """  search offices with given organization and city name """

        organization = request.GET.get('org')
        city = request.GET.get('city')
        page = request.GET.get('page')
        page_size = request.GET.get('page_size')
        officeForm =  OfficeSearchForm(request.GET)
        page_number = page if page else 1
        page_size = page_size if page_size else 10

        if officeForm.is_valid():
            q = Q()
            q =  q & Q(organization__name__icontains=organization)
            search_result = Office.objects.filter(q, city__name__icontains=city, deleted_on=None).values('name', 'description', 'line1', 'line2', 'zipcode', 'organization__name', 'city__name', 'city__state__name', 'city__state__country__name')

            search_result = [{'zipcode': tmp['zipcode'], 'city': tmp['city__name'],
                              'organization': tmp['organization__name'], 'address1': tmp['line1'],
                              'address2': tmp['line2'], 'officeName': tmp['name'],
                              'state': tmp['city__state__name'],
                              'country': tmp['city__state__country__name'],
                              'description': tmp['description']} for tmp in search_result]

            paginator = Paginator(search_result, page_size)
            try:
                current_page  = paginator.page(page_number)
            except PageNotAnInteger:
                page_number = 1
                current_page = paginator.page(page_number)
            except EmptyPage:
                page_number = paginator.num_pages
                current_page = paginator.page(page_number)
            response_data = { "results":list(current_page.object_list), "page_number": page_number, "total_pages":paginator.num_pages}
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            response_data = {"error":officeForm.errors}
            return HttpResponse(json.dumps(response_data), content_type='application/json')
