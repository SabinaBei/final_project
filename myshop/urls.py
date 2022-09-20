from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet

router = routers.SimpleRouter()
router.register(f'product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
# настройка роутера
    path('api/v1/', include(router.urls)),
]
