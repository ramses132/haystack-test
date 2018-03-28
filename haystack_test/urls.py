"""haystack_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import index, sitemap
from django.views.generic.base import TemplateView
from django.views.defaults import (permission_denied, page_not_found,
                                   server_error)


sitemaps = {
    # Fill me with sitemaps
}

urlpatterns = [
    url(r'', include('core.urls')),

    # provide the most basic login/logout functionality
    url(r'^login/$',
        auth_views.login, {'template_name': 'core/login.html'},
        name='core_login'),
    url(r'^logout/$', auth_views.logout, name='core_logout'),

    # enable the admin interface
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    #Rest API
    url(r'^api-auth/', include('rest_framework.urls')),

    # Sitemap
    url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),

    # robots.txt
    url(r'^robots\.txt$',
        TemplateView.as_view(
            template_name='robots.txt', content_type='text/plain')),
]

if settings.DEBUG:
    # Add debug-toolbar
    import debug_toolbar  # noqa
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))

    # Serve media files through Django.
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Show error pages during development
    urlpatterns += [
        url(r'^403/$', permission_denied),
        url(r'^404/$', page_not_found),
        url(r'^500/$', server_error)
    ]
