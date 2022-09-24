from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from products.views import ProductViewSet

router = routers.SimpleRouter()
router.register(f'product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # настройка роутера
    path('api/v1/', include(router.urls)),
    # настройка аутентификации
    path('api-auth/', include('rest_framework.urls')), # login, logout
    path('api/v1/auth/', include('djoser.urls')),  # ссылка на список пользователей
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
