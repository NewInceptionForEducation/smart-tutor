from django.conf.urls import patterns, include, url

from django.conf import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sti.views.home', name='home'),
    # url(r'^sti/', include('sti.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # Ambiente
    url(r'^$', 'tutorinteligente.views.ambiente'),

    # Login e Logout
    url(r'^login/$', "django.contrib.auth.views.login",{
                "template_name": "login_fb.html"}),

    #url(r'^logout/', "django.contrib.auth.views.logout",{
    #            "template_name": "logout.html"}),

    #Social Auth
    url(r'', include('social_auth.urls')),
)
