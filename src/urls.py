from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles import views
from views import IndexView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'customrcare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(template_name = 'customrcare/index.html')),
    url(r'^static/css/bootstrap.min.css', 'django.views.static.serve',
    {'document_root', settings.STATIC_ROOT}),
)
