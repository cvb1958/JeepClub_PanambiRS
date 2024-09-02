from django.contrib import admin

# Register your models here.
from django.contrib.admin.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    search_fields = ('object_repr',)
    list_filter = ('action_time', 'content_type',)
    list_display = ('action_time', 'user', 'content_type', 'tipo', 'object_repr')
    fields = ('action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message', )
    readonly_fields = ('action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'tipo', 'change_message', )

    def tipo(self, obj):
        if obj.is_addition():
            return u"Adicionado"
        elif obj.is_change():
            return u"Modificado"
        elif obj.is_deletion():
            return u"Deletado"

admin.site.register(LogEntry, LogEntryAdmin)

from .models import Cadastro
@admin.register(Cadastro)
class AtividadeAdmin(admin.ModelAdmin):
     list_display = ('nome', 'valor' ,'ano_pago', 'condicao_pago', 'data_pago',)
     list_filter=('condicao_pago',)
     list_editable=('valor',  'condicao_pago', 'data_pago',)
     search_fields=('nome', 'condicao_pago', 'data_pago',)
     ordering=["nome"]