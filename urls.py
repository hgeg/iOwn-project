from django.conf.urls.defaults import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^', include('ihave.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'core.views.landing'),
    (r'^index/$', 'core.views.landing'),
    (r'^signup/$', 'core.views.signup'),
    (r'^signin/$', 'core.views.login'),
    (r'^invite/$', 'core.views.invite'),
    (r'^sendinvite/$', 'core.views.sendinvite'),
    (r'^logout/$', 'core.views.logout'),
    (r'^me/$', 'core.views.profile'),
    (r'^(?P<user>.*)/$', 'core.views.profile'),
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
