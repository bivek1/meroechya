

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('adminpanal/', include('owner.urls', namespace='owner')),
    path('', include('staff.urls', namespace='staff')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
