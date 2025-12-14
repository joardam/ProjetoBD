from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, ProfessorViewSet, AlunoViewSet, MonitorViewSet,
    DisciplinaViewSet, TurmaViewSet, CandidaturaViewSet,
    DocumentoViewSet, CronogramaViewSet, RelatorioViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'monitores', MonitorViewSet)
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'candidaturas', CandidaturaViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'cronogramas', CronogramaViewSet)
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
