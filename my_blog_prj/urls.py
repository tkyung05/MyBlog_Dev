from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('single_pages.urls')),
    path('blog/', include('blog.urls')),

    path('markdownx/', include('markdownx.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

