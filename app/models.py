from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # f-string
        return f'{self.nome} (R$ {self.preco})'


from django.db import models

# Create your models here.
