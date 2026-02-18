from django.urls import include, re_path
from django.conf import settings
import anafora.views
from django.conf.urls.static import static

# import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    re_path(r"^annotate/", include("anafora.urls")),
    re_path(r"^anafora/", include("anafora.urls")),
    re_path(r"^anaforaTest/", include("anaforaTest.urls")),
    re_path(r"^$", anafora.views.index),
    #    url(r'^' + settings.STATIC_URL + '(?P<path>.*)$','django.views.static.serve', {'document_root': settings.STATIC_ROOT}  ),
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
