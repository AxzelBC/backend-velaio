from django.urls import path
from registros import views

urlpatterns = [
    ################################### Noticias ###################################
    path("noticias/create", views.NoticiasCreateView.as_view(), name="noticias_create"),
    path("noticias/list", views.NoticiasListView.as_view(), name="noticias_list"),
    path(
        "noticias/update/<int:pk>",
        views.NoticiasUpdateView.as_view(),
        name="noticias_update",
    ),
    path(
        "noticias/delete/<int:pk>",
        views.NoticiasDeleteView.as_view(),
        name="noticias_delete",
    ),
    ################################### Noticias ###################################
    path("tiempo/create", views.TiempoCreateView.as_view(), name="tiempo_create"),
    path("tiempo/list", views.TiempoListView.as_view(), name="tiempo_list"),
    path(
        "tiempo/update/<int:pk>", views.TiempoUpdateView.as_view(), name="tiempo_update"
    ),
    path(
        "tiempo/delete/<int:pk>", views.TiempoDeleteView.as_view(), name="tiempo_delete"
    ),
]
