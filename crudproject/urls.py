from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from crudapp import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewset)
router.register(r'passports', views.PassportViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)