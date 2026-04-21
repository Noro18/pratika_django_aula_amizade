from django.urls import path
from myapp import views

urlpatterns = [
    # page routing
    path("", views.home, name="home"),
    path("konaba", views.konaba, name="konaba"),

    # CRUD
    path("lista-estudante", views.lista_estudante, name="lista"),
    path("reg/estudante", views.add_estudante, name="add"),
    path("del/estudante/<uuid:id>", views.delete_estudante, name="delete"),
    path("edit/estudante/<uuid:id>", views.edit_estudante, name="edit"),

    # filter
    path("lista-dep", views.listadep, name="listadep"),
    path("lista/dep/estudante/<uuid:id>", views.estudante_dep, name="estudante-dep"),
    
    # auth
    path("loginpage", views.loginpage, name="loginpage"),
    path("logout", views.logout_user, name="logout"),
    
]
