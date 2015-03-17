from django.conf.urls import patterns, include, url
from office.views import OfficeSearchView
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'customrcare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^office/search', OfficeSearchView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
