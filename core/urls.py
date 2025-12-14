from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, ProfessorViewSet, AlunoViewSet, MonitorViewSet,
    DisciplinaViewSet, TurmaViewSet, CandidaturaViewSet,
    DocumentoViewSet, CronogramaViewSet, RelatorioViewSet,
    # Reports
    relatorios_pendentes, cronogramas_vigentes, candidaturas_finalizadas,
    turmas_com_demanda, ficha_monitor, mapeamento_alunos,
    volume_documentacao, media_carga_horaria, disciplinas_multiplas_turmas,
    contatos_administrativos, relatorio_unificado, ultima_atividade,
    relatorios_bd
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
    # Reports
    path('relatorios/pendentes/', relatorios_pendentes, name='relatorios_pendentes'),
    path('relatorios/cronogramas/', cronogramas_vigentes, name='cronogramas_vigentes'),
    path('relatorios/candidaturas/', candidaturas_finalizadas, name='candidaturas_finalizadas'),
    path('relatorios/turmas-demanda/', turmas_com_demanda, name='turmas_com_demanda'),
    path('relatorios/ficha-monitor/', ficha_monitor, name='ficha_monitor'),
    path('relatorios/mapeamento-alunos/', mapeamento_alunos, name='mapeamento_alunos'),
    path('relatorios/volume-documentacao/', volume_documentacao, name='volume_documentacao'),
    path('relatorios/media-carga/', media_carga_horaria, name='media_carga_horaria'),
    path('relatorios/disciplinas-multiplas/', disciplinas_multiplas_turmas, name='disciplinas_multiplas_turmas'),
    path('relatorios/contatos-adm/', contatos_administrativos, name='contatos_administrativos'),
    path('relatorios/unificado/', relatorio_unificado, name='relatorio_unificado'),
    path('relatorios/ultima-atividade/', ultima_atividade, name='ultima_atividade'),
    path('relatorios/bd/', relatorios_bd, name='relatorios_bd'),
]
