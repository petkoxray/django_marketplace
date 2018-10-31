from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('', include('pages.urls')),
                  path('admin/', admin.site.urls),
                  path('categories/', include('categories.urls', namespace='categories')),
                  # path('ads/', include('ads.urls', namespace='ads')),
                  path('users/', include('users.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
