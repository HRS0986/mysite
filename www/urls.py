from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   url(r'^favicon.ico$', redirect_to, {'url': 'http://www.techcreation.sg/media/favicon.ico'}),
   url(r'^$', 'website.home.index'),
   url(r'^base$', 'website.base.index'),
   url(r'^page/(?P<name>.+)$', 'website.page.index'),
   
   url(r'^about$', 'website.about.index'),
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^www/', include('www.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
   url(r'^scheduled$', 'www.scheduled.index'),
)
