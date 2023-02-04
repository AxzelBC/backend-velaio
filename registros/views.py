from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

from registros.models import Noticias, Tiempo
from registros.serializer import NoticiasSerializer, TiempoSerializer

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, permissions


# Vistas de Noticias


# Creación de Noticia
#   Tipo: post
#   Cuerpo
"""
{
    "tipoPeticion": "noticia",
    "enlace": "https://www.elespectador.com/opinion/columnistas/luis-fernando-montoya/columna-del-profe-montoya-campeones-de-la-libertadores/",
    "autor": "Luis Fernando Montoya",
    "titular": "Columna del Profe Montoya: Campeones de la Libertadores",
    "descripcion": "A muchos equipos les cuesta hacer buenas presentaciones y conseguir resultados positivos al comienzo de los torneos. En ese sentido, Atlético Nacional y el Once Caldas, de Manizales —los únicos campeones de América por Colombia—, no han tenido sus mejores presentaciones en el arranque de la Liga y estarán analizando cómo mejorar. Por ahora hay tiempo, pero este va avanzando y rápido se culmina.",
}
"""


@method_decorator(csrf_exempt, name="dispatch")
class NoticiasCreateView(generics.CreateAPIView):
    serializer_class = NoticiasSerializer
    model = Noticias
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"mensaje": "Noticia creado", "data": serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {"mensaje": "Error al crear noticia", "data": serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


# Listar todas las noticias
#   Tipo: get
#   Cuerpo: {}
@method_decorator(csrf_exempt, name="dispatch")
class NoticiasListView(generics.ListAPIView):
    serializer_class = NoticiasSerializer
    model = Noticias
    permission_classes = [permissions.AllowAny]
    queryset = model.objects.all()


# Actualizar una noticia
#   Requisito: pasar {id} por url. Ejemplo: '/noticias/update/1'.
#   Tipo: put
#   Cuerpo
"""
{
    "id": 1,
    "tipoPeticion": "noticia",
    "enlace": "https://www.elespectador.com/opinion/columnistas/luis-fernando-montoya/columna-del-profe-montoya-campeones-de-la-libertadores/",
    "autor": "Luis Fernando",
    "titular": "Columna del Profe Montoya: Campeones de la Libertadores",
    "descripcion": "A muchos equipos les cuesta hacer buenas presentaciones y conseguir resultados positivos al comienzo de los torneos. En ese sentido, Atlético Nacional y el Once Caldas, de Manizales —los únicos campeones de América por Colombia—, no han tenido sus mejores presentaciones en el arranque de la Liga y estarán analizando cómo mejorar. Por ahora hay tiempo, pero este va avanzando y rápido se culmina.",
}
"""


@method_decorator(csrf_exempt, name="dispatch")
class NoticiasUpdateView(generics.UpdateAPIView):
    serializer_class = NoticiasSerializer
    model = Noticias
    permission_classes = [permissions.AllowAny]

    def get_object(self,id):
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            raise Http404("La noticia no existe")

    def put(self, request: Request, *args, **kwargs):
        id = self.kwargs.get("id")
        data = request.data
        noticia = self.get_object(id)
        serializer = self.serializer_class(noticia, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"mensaje": "Actualizado correctamente", "data": serializer.data}
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Eliminar una noticia
#   Requisito: pasar {id} por url. Ejemplo: '/noticias/delete/1'.
#   Tipo: delete
#   Cuerpo: {}
@method_decorator(csrf_exempt, name="dispatch")
class NoticiasDeleteView(generics.DestroyAPIView):
    serializer_class = NoticiasSerializer
    model = Noticias
    permission_classes = [permissions.AllowAny]

    def get_object(self,id):
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            raise Http404("La noticia no existe")

    def delete(self, request: Request, *args, **kwargs):
        id = self.kwargs.get("id")
        noticia = self.get_object(id)
        if noticia.delete():
            response = {"mensaje": "Noticia eliminado"}
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {"mensaje": "Error en el borrado"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


# Vistas de Tiempo


# Creación de Tiempo
#   Tipo: post
#   Cuerpo
"""
{
    "tipoPeticion": "tiempo",
    "enlace": "https://www.elespectador.com/opinion/columnistas/luis-fernando-montoya/columna-del-profe-montoya-campeones-de-la-libertadores/",
    "hora": "18:00:00"
}
"""


@method_decorator(csrf_exempt, name="dispatch")
class TiempoCreateView(generics.CreateAPIView):
    serializer_class = TiempoSerializer
    model = Tiempo
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"mensaje": "Tiempo creado", "data": serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {"mensaje": "Error al crear un time", "data": serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


# Listar todas los registros de tiempo
#   Tipo: get
@method_decorator(csrf_exempt, name="dispatch")
class TiempoListView(generics.ListAPIView):
    serializer_class = TiempoSerializer
    model = Tiempo
    permission_classes = [permissions.AllowAny]
    queryset = model.objects.all()


# Actualizar un tiempo
#   Requisito: pasar {id} por url. Ejemplo: '/tiempo/update/1'.
#   Tipo: put
#   Cuerpo
"""
{
    "id": 1,
    "tipoPeticion": "tiempo",
    "enlace": "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}",
    "hora": "20:00:00"
}
"""


@method_decorator(csrf_exempt, name="dispatch")
class TiempoUpdateView(generics.UpdateAPIView):
    serializer_class = TiempoSerializer
    model = Tiempo
    permission_classes = [permissions.AllowAny]

    def get_object(self,id):
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            raise Http404("El tiempo no existe")

    def put(self, request: Request, *args, **kwargs):
        id = self.kwargs.get("id")
        data = request.data
        tiempo = self.get_object(id)
        serializer = self.serializer_class(tiempo, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"mensaje": "Actualizado correctamente", "data": serializer.data}
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Eliminar una noticia
#   Requisito: pasar {id} por url. Ejemplo: '/tiempo/delete/1'.
#   Tipo: delete
#   Cuerpo: {}
@method_decorator(csrf_exempt, name="dispatch")
class TiempoDeleteView(generics.DestroyAPIView):
    serializer_class = TiempoSerializer
    model = Tiempo
    permission_classes = [permissions.AllowAny]

    def get_object(self,id):
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            raise Http404("El tiempo no existe")

    def delete(self, request: Request, *args, **kwargs):
        id = self.kwargs.get("id")
        tiempo = self.get_object(id)
        if tiempo.delete():
            response = {"mensaje": "Tiempo eliminado"}
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {"mensaje": "Error en el borrado"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
