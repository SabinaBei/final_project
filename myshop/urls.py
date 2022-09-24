from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from products.views import ProductViewSet, CommentView, ProductLikeView, RatingView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


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
    # настройка swaggera
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # настройка комментариев
    path('<int:product_pk>/comment/create/', CommentView.as_view({'post':'create'})),
    # настройка лайков
    path('<int:product_pk>/like/', ProductLikeView.as_view()),
    # настройка рейтинга
    path('<int:product_pk>/rating/', RatingView.as_view({'get': 'list', 'post': 'create'})),
]
