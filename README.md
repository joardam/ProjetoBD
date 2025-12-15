# Sistema de Gerenciamento de Monitorias (SGM)

Este projeto implementa o backend de um sistema acadêmico para gestão de monitorias, desenvolvido com **Django Rest Framework** e **PostgreSQL**. O sistema inclui as 13 consultas SQL fundamentais para geração de relatórios gerenciais.

## 🚀 Como Rodar no GitHub Codespaces

Este repositório está configurado com um *Dev Container*, o que significa que todo o ambiente (Python, Dependências, Banco de Dados) é configurado automaticamente.

### 1. Iniciar o Ambiente
Ao abrir este repositório no GitHub Codespaces, aguarde o terminal configurar o container. O processo automático já executa:
- Instalação das dependências (`pip install -r requirements.txt`).
- Migração do banco de dados (`python manage.py migrate`).

### 2. Popular o Banco de Dados (Carga Inicial)
Para testar todas as funcionalidades e relatórios imediatamente, execute o script de população que cria usuários, turmas, candidaturas e relatórios fictícios coerentes:

1. Certifique-se de que o arquivo `popular_banco.py` está na raiz do projeto.
2. No terminal do Codespaces, execute:

```bash
python manage.py shell < popular_banco.py
```

> **Nota:** Este script limpa o banco de dados antes de recriar os dados para evitar duplicatas.

### 3. Acessar o Sistema
Após rodar o script, o servidor já deve estar rodando (se não estiver, use `python manage.py runserver 0.0.0.0:8000`).

Abra a aba "PORTS" no VS Code e clique no ícone do globo (Open in Browser) na porta 8000.

#### 🔑 Credenciais de Acesso (Geradas pelo Script)

| Perfil | Usuário | Senha |
| :--- | :--- | :--- |
| **Administrador** | `admin_user` | `123` |
| **Professor (BD)** | `prof_banco` | `123` |
| **Aluno (Monitor)** | `aluno_monitor` | `123` |

## 📊 Relatórios Gerenciais (Consultas SQL)

O sistema implementa 13 relatórios baseados em consultas SQL específicas. Acesse-os diretamente pelas URLs abaixo (adicione ao final do endereço do seu ambiente):

| ID | Descrição do Relatório | URL de Acesso |
| :--- | :--- | :--- |
| 01 | Relatórios Pendentes (IS NULL) | `/api/relatorios/pendentes/` |
| 02 | Cronogramas Vigentes (BETWEEN) | `/api/relatorios/cronogramas/` |
| 03 | Candidaturas Finalizadas (IN) | `/api/relatorios/candidaturas/` |
| 04 | Turmas com Demanda (EXISTS) | `/api/relatorios/turmas-demanda/` |
| 05 | Ficha Completa do Monitor (JOINs) | `/api/relatorios/ficha-monitor/` |
| 06 | Mapeamento de Alunos (LEFT JOIN) | `/api/relatorios/mapeamento-alunos/` |
| 07 | Volume de Documentação (COUNT) | `/api/relatorios/volume-documentacao/` |
| 08 | Média de Carga Horária (AVG) | `/api/relatorios/media-carga/` |
| 09 | Disciplinas com Múltiplas Turmas | `/api/relatorios/disciplinas-multiplas/` |
| 10 | Contatos Administrativos (NESTED) | `/api/relatorios/contatos-adm/` |
| 11 | Relatório Unificado (UNION) | `/api/relatorios/unificado/` |
| 12 | Última Atividade (ORDER BY) | `/api/relatorios/ultima-atividade/` |
| 13 | Relatórios de BD (Complexa) | `/api/relatorios/bd/` |

## 🛠 Comandos Úteis

Se precisar reiniciar o ambiente ou criar um superusuário manualmente:

**Criar Superusuário Manualmente:**
```bash
python manage.py createsuperuser
```

**Rodar Migrações (se alterar modelos):**
```bash
python manage.py makemigrations core
python manage.py migrate
```

**Reiniciar o Servidor:**
```bash
python manage.py runserver 0.0.0.0:8000
```