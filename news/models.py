from django.db import models
class Giornalista(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20) 

    def _str_(self):
        return self.nome + " " + self.cognome

class Articolo(models.Model):
    titolo = models.CharField(max_length=20)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def _str_(self):
        return self.titolo
