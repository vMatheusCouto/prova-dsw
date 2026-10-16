from django.db import models

# Create your models here.
class Modalidade(models.Model):
    TIPOS = {
        "individual": "Individual",
        "coletiva": "Coletiva"
    }
    nome = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(blank=False, choices=TIPOS)
    max_atletas = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]
        
        verbose_name = "modalidade"
        verbose_name_plural = "modalidades"
    

class Equipe(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=50, unique=True)
    cor = models.CharField(max_length=7)
    criada_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]
        
        verbose_name = "equipe"
        verbose_name_plural = "equipes"
    
    
class Tecnico(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=50)

    equipe = models.OneToOneField("Equipe", related_name="tecnico", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]
        
        verbose_name = "técnico"
        verbose_name_plural = "técnicos"
    
class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()
    
    equipe = models.ForeignKey("Equipe", related_name="atletas", null=True, blank=True, on_delete=models.PROTECT)
    modalidades = models.ManyToManyField("Modalidade", related_name="atletas", blank=True)

    def __str__(self):
            return self.nome
    
    class Meta:
        ordering = ["nome"]
        
        verbose_name = "atleta"
        verbose_name_plural = "atletas"