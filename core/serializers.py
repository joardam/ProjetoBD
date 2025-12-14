from rest_framework import serializers
from .models import (
    Usuario, Professor, Aluno, Monitor,
    Disciplina, Turma, Candidatura,
    Documento, Cronograma, Relatorio
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'titulacao', 'area_atuacao']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'matricula', 'curso', 'periodo']

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'matricula', 'curso', 'periodo', 'carga_horaria']

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class CandidaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatura
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class CronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cronograma
        fields = '__all__'

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'
