from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('post/create/', views.create_post, name='create_post'),  # Cria posts
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Detalhes dos posts
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),  # Edita post
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # Exclui post
]
