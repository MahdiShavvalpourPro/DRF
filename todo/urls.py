from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo import views
from todo.views import todo_detail_view, ManageTodos
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


# region import for jwt

schema_view = get_swagger_view(title='Pastebin API')
# endregion

router = DefaultRouter()
router.register('', views.TodosViewSetApiView)

user_router = DefaultRouter()
user_router.register('', views.UserViewSetApi)

urlpatterns = [
    path('', views.all_todos),
    # path('', include(router.urls)),
#     path('<int:todo_id>', todo_detail_view),
#     path('cbv/', views.ManageTodos.as_view()),
#     path('cbv/<int:pk>', views.ManageTodoDetail.as_view()),
#     path('mixin/', views.TodosListMixinApiView.as_view()),
#     path('mixin/<int:pk>', views.TodosDetailMixinApiView.as_view()),
#     path('generics/', views.TodosGenericCreateListApiView.as_view()),
#     path('generics/<pk>', views.TodosGenericUpdateDestroyApiView.as_view()),
    path('viewsets/', include(router.urls)),
#     path('userviewset', include(user_router.urls)),
#     path('auth-token/', obtain_auth_token, name='generate_auth_token'),
#     path('new-auth-token/', views.CustomAuthToken.as_view()),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),


]
