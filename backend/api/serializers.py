from rest_framework import serializers
from .models import Projeto, Tarefa, User

# Serializer para o modelo de Usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer para o modelo de Projeto
class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'descricao', 'criado_em', 'atualizado_em']

# Serializer para o modelo de Tarefa
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'descricao', 'status', 'projeto', 'criado_em', 'atualizado_em']
