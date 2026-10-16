from django.contrib import admin
from jogos.models import Atleta, Equipe, Tecnico, Modalidade

class TecnicoInline(admin.TabularInline):
    model = Tecnico
    extra = 1
    

# Register your models here.
@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ["nome", "matricula", "equipe"]
    search_fields = ["nome"]
    list_filter = ["equipe","modalidades"]

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    @admin.display(description="Quantidade Atletas")
    def quantidade_atletas(self):
        return self.atletas.count()
        
    list_display = ["nome", "curso", quantidade_atletas]
    inlines = [TecnicoInline]
    

admin.site.register(Tecnico)
admin.site.register(Modalidade)