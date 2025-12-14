from rest_framework import viewsets
from .models import (
    Usuario, Professor, Aluno, Monitor,
    Disciplina, Turma, Candidatura,
    Documento, Cronograma, Relatorio
)
from .serializers import (
    UsuarioSerializer, ProfessorSerializer, AlunoSerializer, MonitorSerializer,
    DisciplinaSerializer, TurmaSerializer, CandidaturaSerializer,
    DocumentoSerializer, CronogramaSerializer, RelatorioSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class CandidaturaViewSet(viewsets.ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class CronogramaViewSet(viewsets.ModelViewSet):
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
