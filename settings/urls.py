from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .settings import MEDIA_URL, MEDIA_ROOT
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    *static(MEDIA_URL, document_root=MEDIA_ROOT)
]

# swagger
urlpatterns += doc_urls
