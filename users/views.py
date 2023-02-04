from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth import authenticate

from users.models import Usuario
from users.serializer import UsuarioSerializer
from users.tokens import create_jwt_pair_for_user

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, permissions


# Vista de usuario


# Crear usuario
@method_decorator(csrf_exempt, name="dispatch")
class UsuarioCreateView(generics.CreateAPIView):
    serializer_class = UsuarioSerializer
    model = Usuario
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"mensaje": "Usuario creado", "data": serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)


# Modificar usuario
@method_decorator(csrf_exempt, name="dispatch")
class UsuarioUpdateView(generics.UpdateAPIView):
    serializer_class = UsuarioSerializer
    model = Usuario
    permission_classes = [permissions.AllowAny]

    def get_object(self, id):
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            raise Http404("El usuario no existe")

    def put(self, request: Request, *args, **kwargs):
        id = self.kwargs.get("id")
        data = request.data
        usuario = self.get_object(id)
        serializer = self.serializer_class(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"mensaje": "Actualizado correctamente", "data": serializer.data}
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Borrar usuario
@method_decorator(csrf_exempt, name="dispatch")
class UsuarioDeleteView(generics.DestroyAPIView):
    serializer_class = UsuarioSerializer
    model = Usuario
    permission_classes = [permissions.AllowAny]

    def get_object(self, id):
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            raise Http404("El usuario no existe")

    def delete(self, request: Request, *args, **kwargs):
        id = self.kwargs.get("id")
        usuario = self.get_object(id)
        if usuario.delete():
            response = {"mensaje": "Usuario eliminado"}
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {"mensaje": "Error en el borrado"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


# Inicio de sesión
@method_decorator(csrf_exempt, name="dispatch")
class UsuarioLoginView(APIView):
    serializer_class = UsuarioSerializer
    model = Usuario
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        print(repr(email))
        print(repr(password))
        usuario = authenticate(email=email, password=password)
        print(repr(usuario))
        if usuario is not None:
            tokens = create_jwt_pair_for_user(usuario)
            serializer = self.model(usuario, many=False)
            response = {
                "login": True,
                "message": "Logueado correctamente",
                "tokens": tokens,
                "data": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {"login": False, "mensaje": "Correo o contraseña invalidos"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
