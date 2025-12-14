from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Usuario, Professor, Aluno, Monitor,
    Disciplina, Turma, Candidatura,
    Documento, Cronograma, Relatorio
)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    pass

@admin.register(Professor)
class ProfessorAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Acadêmicas', {'fields': ('titulacao', 'area_atuacao')}),
    )

@admin.register(Aluno)
class AlunoAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Acadêmicas', {'fields': ('matricula', 'curso', 'periodo')}),
    )

@admin.register(Monitor)
class MonitorAdmin(AlunoAdmin):
    fieldsets = AlunoAdmin.fieldsets + (
        ('Monitoria', {'fields': ('carga_horaria',)}),
    )

admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Candidatura)
admin.site.register(Documento)
admin.site.register(Cronograma)
admin.site.register(Relatorio)
