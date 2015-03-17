import json
from django.http import JsonResponse
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
from .forms import OfficeDetailsForm
from city.models import City
from django import forms


class OfficeSearchView(ListView):

    def get(self, request, *args, **Kwargs):

        response_data ={}
        print("request data is", dir(request))
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        search = request.GET.get('q')
        city = request.GET.get('city')
        q = Q()
        page = 1
        page_size =10
        if search:
            q =  q & Q(organization__name__icontains=search)
            print("called in if condition@@@@@@@@@@@@@@@@@")
            office_info = Office.objects.filter(q, city__name__icontains=city)
            print("value of q is", office_info)
            print("get fn called!!!!!!!!!!")
            #form = OfficeDetailsForm()
            paginator = Paginator(office_info, page_size)
            try:
                office_search  = paginator.page(page)
            except PageNotAnInteger:
                office_search = paginator.page(1)
            except EmptyPage:
                office_search = paginator.page(paginator.num_pages)

        response_data['result'] = office_search
        print('contact details::', office_search)
        return HttpResponse(json.dumps(response_data), mimetype='application/json')
