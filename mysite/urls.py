from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views import static


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^testapp/', include('testapp.urls')),
	
    url(r'^$', include('home.urls')),

    url(r"^static/(?P<path>.*)$", static.serve, 
        {'document_root':settings.STATIC_ROOT}, name='static'),
)
