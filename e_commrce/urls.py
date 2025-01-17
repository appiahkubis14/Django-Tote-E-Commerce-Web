
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('portal/', include("portal.urls")),
    path('', include('store.urls')),
    # path('category/',include('category.urls')),
    path('accounts/', include('allauth.urls')),
    # path('', include('authentication.urls')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
