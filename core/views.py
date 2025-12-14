from django.shortcuts import render
from django.db import connection
from rest_framework import viewsets
from .utils import dictfetchall
from .serializers import (
    UsuarioSerializer, ProfessorSerializer, AlunoSerializer, MonitorSerializer,
    DisciplinaSerializer, TurmaSerializer, CandidaturaSerializer,
    DocumentoSerializer, CronogramaSerializer, RelatorioSerializer
)
from .models import (
    Usuario, Professor, Aluno, Monitor,
    Disciplina, Turma, Candidatura,
    Documento, Cronograma, Relatorio
)

# --- ViewSets para a API (Faltavam no arquivo original) ---

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


def relatorios_pendentes(request):
    """
    Consulta 01: Relatórios Pendentes de Avaliação
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT M.aluno_ptr_id as monitor_id, A.matricula, R.data_envio, R.tipo 
            FROM academico_relatorio R
            JOIN academico_monitor M ON R.monitor_id = M.aluno_ptr_id
            JOIN academico_aluno A ON M.aluno_ptr_id = A.usuario_ptr_id
            WHERE R.nota IS NULL 
        """)
        relatorios = dictfetchall(cursor)
    return render(request, 'core/reports/relatorios_pendentes.html', {'relatorios': relatorios})

def cronogramas_vigentes(request):
    """
    Consulta 02: Cronogramas Vigentes
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT descricao, data_inicio, data_fim 
            FROM academico_cronograma 
            WHERE data_inicio BETWEEN '2025-01-01' AND '2025-06-30'
        """)
        cronogramas = dictfetchall(cursor)
    return render(request, 'core/reports/cronogramas_vigentes.html', {'cronogramas': cronogramas})

def candidaturas_finalizadas(request):
    """
    Consulta 03: Candidaturas Finalizadas
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT C.id, A.matricula, C.status 
            FROM academico_candidatura C
            JOIN academico_aluno A ON C.aluno_id = A.usuario_ptr_id
            WHERE C.status IN ('APROVADA', 'REJEITADA')
        """)
        candidaturas = dictfetchall(cursor)
    return render(request, 'core/reports/candidaturas_finalizadas.html', {'candidaturas': candidaturas})

def turmas_com_demanda(request):
    """
    Consulta 04: Turmas com Demanda
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT T.id, D.nome_disciplina as disciplina, T.ano_semestre 
            FROM academico_turma T
            JOIN academico_disciplina D ON T.disciplina_id = D.id
            WHERE EXISTS (SELECT 1 FROM academico_candidatura C WHERE C.turma_id = T.id)
        """)
        turmas = dictfetchall(cursor)
    return render(request, 'core/reports/turmas_com_demanda.html', {'turmas': turmas})

def ficha_monitor(request):
    """
    Consulta 05: Ficha Completa do Monitor
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT U_ALUNO.first_name as aluno, D.nome_disciplina as disciplina, U_PROF.first_name as orientador
            FROM academico_monitor M
            JOIN academico_aluno A ON M.aluno_ptr_id = A.usuario_ptr_id
            JOIN academico_usuario U_ALUNO ON A.usuario_ptr_id = U_ALUNO.id
            JOIN academico_turma T ON M.turma_id = T.id
            JOIN academico_disciplina D ON T.disciplina_id = D.id
            JOIN academico_professor P ON T.professor_id = P.usuario_ptr_id
            JOIN academico_usuario U_PROF ON P.usuario_ptr_id = U_PROF.id
        """)
        monitores = dictfetchall(cursor)
    return render(request, 'core/reports/ficha_monitor.html', {'monitores': monitores})

def mapeamento_alunos(request):
    """
    Consulta 06: Mapeamento de Alunos e Monitorias
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT U.first_name, M.carga_horaria
            FROM academico_aluno A
            JOIN academico_usuario U ON A.usuario_ptr_id = U.id
            LEFT JOIN academico_monitor M ON A.usuario_ptr_id = M.aluno_ptr_id
        """)
        alunos = dictfetchall(cursor)
    return render(request, 'core/reports/mapeamento_alunos.html', {'alunos': alunos})

def volume_documentacao(request):
    """
    Consulta 07: Volume de Documentação
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT candidatura_id, COUNT(id) as total_documentos 
            FROM academico_documento 
            GROUP BY candidatura_id
        """)
        documentos = dictfetchall(cursor)
    return render(request, 'core/reports/volume_documentacao.html', {'documentos': documentos})

def media_carga_horaria(request):
    """
    Consulta 08: Média de Carga Horária
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT AVG(M.carga_horaria) as media_horas 
            FROM academico_monitor M
            JOIN academico_aluno A ON M.aluno_ptr_id = A.usuario_ptr_id
            JOIN academico_usuario U ON A.usuario_ptr_id = U.id
            WHERE U.is_active = TRUE
        """)
        media = dictfetchall(cursor)
    return render(request, 'core/reports/media_carga_horaria.html', {'media': media})

def disciplinas_multiplas_turmas(request):
    """
    Consulta 09: Disciplinas com Múltiplas Turmas
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT D.nome_disciplina, COUNT(T.id) as qtd_turmas
            FROM academico_disciplina D
            JOIN academico_turma T ON D.id = T.disciplina_id
            GROUP BY D.nome_disciplina
            HAVING COUNT(T.id) > 1
        """)
        disciplinas = dictfetchall(cursor)
    return render(request, 'core/reports/disciplinas_multiplas_turmas.html', {'disciplinas': disciplinas})

def contatos_administrativos(request):
    """
    Consulta 10: Contatos Administrativos
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT email, first_name 
            FROM academico_usuario 
            WHERE id IN (SELECT usuario_ptr_id FROM academico_funcionarioadm)
        """)
        contatos = dictfetchall(cursor)
    return render(request, 'core/reports/contatos_administrativos.html', {'contatos': contatos})

def relatorio_unificado(request):
    """
    Consulta 11: Relatório Unificado de Membros
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT U.first_name as nome, 'Professor' as tipo 
            FROM academico_professor P JOIN academico_usuario U ON P.usuario_ptr_id = U.id
            UNION
            SELECT U.first_name as nome, 'Aluno' as tipo 
            FROM academico_aluno A JOIN academico_usuario U ON A.usuario_ptr_id = U.id
        """)
        membros = dictfetchall(cursor)
    return render(request, 'core/reports/relatorio_unificado.html', {'membros': membros})

def ultima_atividade(request):
    """
    Consulta 12: Última Atividade de Inscrição
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT U.first_name as nome_candidato, C.data_submissao
            FROM academico_candidatura C
            JOIN academico_aluno A ON C.aluno_id = A.usuario_ptr_id
            JOIN academico_usuario U ON A.usuario_ptr_id = U.id
            ORDER BY C.data_submissao DESC
        """)
        atividades = dictfetchall(cursor)
    return render(request, 'core/reports/ultima_atividade.html', {'atividades': atividades})

def relatorios_bd(request):
    """
    Consulta 13: Relatórios por Disciplina Específica
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT R.tipo, R.conteudo, U.first_name as monitor
            FROM academico_relatorio R
            JOIN academico_monitor M ON R.monitor_id = M.aluno_ptr_id
            JOIN academico_aluno A ON M.aluno_ptr_id = A.usuario_ptr_id
            JOIN academico_usuario U ON A.usuario_ptr_id = U.id
            WHERE M.turma_id IN (
                SELECT T.id FROM academico_turma T
                JOIN academico_disciplina D ON T.disciplina_id = D.id
                WHERE D.nome_disciplina = 'Banco de Dados'
            )
        """)
        relatorios = dictfetchall(cursor)
    return render(request, 'core/reports/relatorios_bd.html', {'relatorios': relatorios})
