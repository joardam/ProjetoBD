import os
import django
from datetime import date
from django.db import transaction
from core.models import (
    Usuario, Professor, Aluno, Monitor, FuncionarioAdm,
    Disciplina, Turma, Candidatura, Documento, Cronograma, Relatorio
)

print("Iniciando povoamento do banco de dados...")

with transaction.atomic():
    
    # --- Limpeza inicial ---
    print("Limpando dados antigos...")
    Relatorio.objects.all().delete()
    Cronograma.objects.all().delete()
    Documento.objects.all().delete()
    Candidatura.objects.all().delete()
    Monitor.objects.all().delete()
    Turma.objects.all().delete()
    Disciplina.objects.all().delete()
    Aluno.objects.all().delete()
    Professor.objects.all().delete()
    FuncionarioAdm.objects.all().delete()
    Usuario.objects.all().delete()

    # --- 1. Criação de Usuários e Perfis ---
    
    # Funcionario Administrativo
    print("Criando Administrativo...")
    # Cria o usuário base primeiro e depois promove (pois não tem campos extras obrigatórios)
    user_adm = Usuario.objects.create_user(
        username='admin_user', 
        email='admin@uf.br', 
        password='123', 
        first_name='Carlos', 
        last_name='Admin'
    )
    adm = FuncionarioAdm(usuario_ptr=user_adm)
    adm.save_base(raw=True) 

    # Professores
    print("Criando Professores...")
    # CORREÇÃO: Passando campos obrigatórios dentro do create_user
    prof1 = Professor.objects.create_user(
        username='prof_banco', 
        email='prof.bd@uf.br', 
        password='123', 
        first_name='Ana', 
        last_name='Silva',
        titulacao='Doutora',
        area_atuacao='Banco de Dados'
    )

    prof2 = Professor.objects.create_user(
        username='prof_geral', 
        email='prof.dev@uf.br', 
        password='123', 
        first_name='Roberto', 
        last_name='Costa',
        titulacao='Mestre',
        area_atuacao='Engenharia de Software'
    )

    # Alunos
    print("Criando Alunos...")
    # CORREÇÃO: Passando campos obrigatórios (matricula, curso, periodo) dentro do create_user
    
    # Aluno 1: Vai ser Monitor de BD
    aluno1 = Aluno.objects.create_user(
        username='aluno_monitor', 
        email='joao.monitor@uf.br', 
        password='123', 
        first_name='João', 
        last_name='Souza',
        matricula='2023001',
        curso='Ciência da Computação',
        periodo=4
    )

    # Aluno 2: Candidato Pendente
    aluno2 = Aluno.objects.create_user(
        username='aluno_candidato', 
        email='maria.cand@uf.br', 
        password='123', 
        first_name='Maria', 
        last_name='Lima',
        matricula='2023002',
        curso='Engenharia da Computação',
        periodo=3
    )

    # Aluno 3: Candidato Rejeitado
    aluno3 = Aluno.objects.create_user(
        username='aluno_rejeitado', 
        email='pedro.rej@uf.br', 
        password='123', 
        first_name='Pedro', 
        last_name='Santos',
        matricula='2023003',
        curso='Sistemas de Informação',
        periodo=5
    )

    # Aluno 4: Sem vínculo
    aluno4 = Aluno.objects.create_user(
        username='aluno_inativo', 
        email='lucas.nada@uf.br', 
        password='123', 
        first_name='Lucas', 
        last_name='Ferreira',
        matricula='2023004',
        curso='Redes',
        periodo=1
    )

    # --- 2. Acadêmico ---

    print("Criando Disciplinas e Turmas...")
    disc_bd = Disciplina.objects.create(nome_disciplina='Banco de Dados', codigo_disciplina='COMP001')
    disc_web = Disciplina.objects.create(nome_disciplina='Desenvolvimento Web', codigo_disciplina='COMP002')

    turma_bd = Turma.objects.create(ano_semestre='2025.1', disciplina=disc_bd, professor=prof1)
    turma_web_1 = Turma.objects.create(ano_semestre='2025.1', disciplina=disc_web, professor=prof2)
    turma_web_2 = Turma.objects.create(ano_semestre='2025.2', disciplina=disc_web, professor=prof2)

    # --- 3. Processo Seletivo ---

    print("Criando Candidaturas...")
    cand1 = Candidatura.objects.create(aluno=aluno1, turma=turma_bd, status='APROVADA')
    cand2 = Candidatura.objects.create(aluno=aluno2, turma=turma_web_1, status='PENDENTE')
    cand3 = Candidatura.objects.create(aluno=aluno3, turma=turma_web_1, status='REJEITADA')

    # Cronograma
    Cronograma.objects.create(
        candidatura=cand2,
        descricao='Processo Seletivo Monitoria 2025.1',
        data_inicio=date(2025, 2, 1),
        data_fim=date(2025, 6, 15)
    )

    # Documentos
    Documento.objects.create(candidatura=cand1, titulo='Histórico Escolar', tipo='PDF', data_emissao=date(2024, 12, 10))
    Documento.objects.create(candidatura=cand1, titulo='Currículo Lattes', tipo='PDF', data_emissao=date(2024, 12, 11))
    Documento.objects.create(candidatura=cand2, titulo='Carta de Intenção', tipo='DOCX', data_emissao=date(2025, 1, 15))

    # --- 4. Monitoria ---

    print("Criando Monitores e Relatórios...")
    # Promovendo Aluno 1 a Monitor
    monitor_bd = Monitor(
        aluno_ptr=aluno1, 
        carga_horaria=12,
        turma=turma_bd,
        ativo=True
    )
    monitor_bd.save_base(raw=True)

    # Relatórios
    Relatorio.objects.create(
        monitor=monitor_bd,
        tipo='Mensal - Março',
        conteudo='Auxílio aos alunos com MER e DER.',
        nota=None
    )

    Relatorio.objects.create(
        monitor=monitor_bd,
        tipo='Mensal - Abril',
        conteudo='Correção de exercícios de SQL Avançado.',
        nota=9.5
    )

print("--------------------------------------------------")
print("Povoamento concluído com sucesso!")