from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo import views
from todo.views import todo_detail_view, ManageTodos

router = DefaultRouter()
router.register('', views.TodosViewSetApiView)

user_router = DefaultRouter()
user_router.register('', views.UserViewSetApi)


urlpatterns = [
    path('', views.all_todos),
    # path('', include(router.urls)),
    path('<int:todo_id>', todo_detail_view),
    path('cbv/', views.ManageTodos.as_view()),
    path('cbv/<int:pk>', views.ManageTodoDetail.as_view()),
    path('mixin/', views.TodosListMixinApiView.as_view()),
    path('mixin/<int:pk>', views.TodosDetailMixinApiView.as_view()),
    path('generics/', views.TodosGenericCreateListApiView.as_view()),
    path('generics/<pk>', views.TodosGenericUpdateDestroyApiView.as_view()),
    path('viewsets/', include(router.urls)),
    path('userviewset', include(user_router.urls))
]
