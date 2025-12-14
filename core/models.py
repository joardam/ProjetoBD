from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    """
    Modelo base de usuário.
    Atributos: nome, email, senha (herdados de AbstractUser).
    """
    class Meta:
        db_table = 'academico_usuario'

    def __str__(self):
        return self.username

class Professor(Usuario):
    """
    Professor herda de Usuario.
    """
    titulacao = models.CharField(max_length=100)
    area_atuacao = models.CharField(max_length=100)

    class Meta:
        db_table = 'academico_professor'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

class Aluno(Usuario):
    """
    Aluno herda de Usuario.
    """
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    periodo = models.IntegerField()

    class Meta:
        db_table = 'academico_aluno'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Monitor(Aluno):
    """
    Monitor herda de Aluno.
    """
    carga_horaria = models.IntegerField()

    class Meta:
        db_table = 'academico_monitor'
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitores'

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=100)
    codigo_disciplina = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'academico_disciplina'
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome_disciplina

class Turma(models.Model):
    ano_semestre = models.CharField(max_length=6) # Ex: 2023.1
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='turmas')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='turmas')

    class Meta:
        db_table = 'academico_turma'
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        return f"{self.disciplina.nome_disciplina} - {self.ano_semestre}"

class Candidatura(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADA', 'Aprovada'),
        ('REJEITADA', 'Rejeitada'),
    ]
    data_submissao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='candidaturas')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='candidaturas')

    class Meta:
        db_table = 'academico_candidatura'
        verbose_name = 'Candidatura'
        verbose_name_plural = 'Candidaturas'

class Documento(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    data_emissao = models.DateField()
    candidatura = models.ForeignKey(Candidatura, on_delete=models.CASCADE, related_name='documentos')

    class Meta:
        db_table = 'academico_documento'
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

class Cronograma(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    candidatura = models.OneToOneField(Candidatura, on_delete=models.CASCADE, related_name='cronograma')

    class Meta:
        db_table = 'academico_cronograma'
        verbose_name = 'Cronograma'
        verbose_name_plural = 'Cronogramas'

class Relatorio(models.Model):
    tipo = models.CharField(max_length=50)
    data_envio = models.DateField(auto_now_add=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, related_name='relatorios')

    class Meta:
        db_table = 'academico_relatorio'
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'
