from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetoViewSet, TarefaViewSet, UserViewSet

# Criando um router para registrar os ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'projetos', ProjetoViewSet, basename='projeto')
router.register(r'tarefas', TarefaViewSet, basename='tarefa')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),  # Rotas de autenticação
    path('auth/', include('djoser.urls.jwt')),  # Rotas JWT para login/logout
]
