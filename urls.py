from django.conf.urls.defaults import patterns, include, url
from ihave import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ihave.views.home', name='home'),
    # url(r'^ihave/', include('ihave.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'ihave.core.views.landing'),
    (r'^index/$', 'ihave.core.views.landing'),
    (r'^(?P<user>.*)/$', 'ihave.core.views.profile'),
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
