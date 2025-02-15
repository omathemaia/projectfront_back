from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Projeto, Tarefa, User
from .serializers import ProjetoSerializer, TarefaSerializer, UserSerializer

# ViewSet para usuários (somente leitura)
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para Projetos
class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para Tarefas
class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]
