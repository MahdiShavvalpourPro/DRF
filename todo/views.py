# region imports

from rest_framework_swagger.views import get_swagger_view
from http.client import responses
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from todo.models import Todo
from .serilizers import TodoSerializer, UserSerializer

from rest_framework import mixins, generics
from rest_framework import viewsets

from django.contrib.auth import get_user_model

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# endregion

# Create your views here.

# region function base view
@api_view(['Get', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_view(request: Request, todo_id: int):
    try:
        todo: Todo = Todo.objects.get(pk=todo_id)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = TodoSerializer(todo)
        return Response(serialize.data, status.HTTP_200_OK)

    if request.method == 'PUT':
        serialize = TodoSerializer(todo, request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


# endregion

# region class base view

class ManageTodos(APIView):
    def get(self, request: Request):
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)


class ManageTodoDetail(APIView):
    def get_object(self, todo_id: int):
        try:
            todo = Todo.objects.get(pk=todo_id)
            return todo
        except todo.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        serialize = TodoSerializer(todo, request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        todo = todo = self.get_object(pk)
        todo.delete()


# endregion

# region Mixin

class TodosListMixinApiView(mixins.CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class TodosDetailMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                              GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk: int):
        return self.update(request, pk)

    def delete(self, request: Request, pk: int):
        return self.destroy(request, pk)


# endregion


class Pagination(PageNumberPagination):
    page_size = 5


# region api by Genercis


class TodosGenericCreateListApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = LimitOffsetPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class TodosGenericUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer


# endregion

# region View Set Api


class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = Pagination


# endregion


# region User
user = get_user_model()


class UserViewSetApi(viewsets.ModelViewSet):
    queryset = user.objects.order_by('first_name').all()
    serializer_class = UserSerializer


# endregion

# region Make a new token


class CustomAuthToken(APIView):
    def post(setlf, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not Null:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': Token.key})
        return Response({'error': 'Invalid credentials'}, status=400)

# endregion



