from django.urls import path
from users import views

urlpatterns = [
    path("auth", views.UsuarioLoginView.as_view(), name="auth"),
    path("create", views.UsuarioCreateView.as_view(), name="usuario_create"),
    path(
        "update/<int:id>",
        views.UsuarioUpdateView.as_view(),
        name="usuario_update",
    ),
    path(
        "delete/<int:id>",
        views.UsuarioDeleteView.as_view(),
        name="usuario_delete",
    ),
]
