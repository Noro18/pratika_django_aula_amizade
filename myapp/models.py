from django.db import models
import uuid

class Departamento(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    naran_dep = models.CharField(max_length=15, verbose_name="Naran Departamanto", unique=True, blank=False)
    
    def __str__(self):
        return self.naran_dep

class Estudante(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nre = models.CharField(max_length=11, unique=True, blank=False, verbose_name="N.R.E")
    naran_estudante = models.CharField(max_length=100, blank=False, verbose_name="Naran Estudante")
    sexu = models.CharField(max_length=4, choices=[("Mane", "Mane"), ("Feto", "Feto")], default="Mane")
    idade = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    hela_fatin = models.CharField(max_length=50, blank=True, default="", verbose_name="Hela Fatin")
    email = models.EmailField(max_length=50, blank=True)
    nu_telefone = models.CharField(max_length=8, verbose_name="Numeru Telefone")
    imajen = models.FileField(upload_to="imajen")
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.naran_estudante

