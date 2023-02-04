from django.urls import path
from registros import views

urlpatterns = [
    ################################### Noticias ###################################
    path("noticias/create", views.NoticiasCreateView.as_view(), name="noticias_create"),
    path("noticias/list", views.NoticiasListView.as_view(), name="noticias_list"),
    path(
        "noticias/update/<int:id>",
        views.NoticiasUpdateView.as_view(),
        name="noticias_update",
    ),
    path(
        "noticias/delete/<int:id>",
        views.NoticiasDeleteView.as_view(),
        name="noticias_delete",
    ),
    ################################### Noticias ###################################
    path("tiempo/create", views.TiempoCreateView.as_view(), name="tiempo_create"),
    path("tiempo/list", views.TiempoListView.as_view(), name="tiempo_list"),
    path(
        "tiempo/update/<int:id>", views.TiempoUpdateView.as_view(), name="tiempo_update"
    ),
    path(
        "tiempo/delete/<int:id>", views.TiempoDeleteView.as_view(), name="tiempo_delete"
    ),
]
