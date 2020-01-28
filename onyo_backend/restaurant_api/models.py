from django.db import models


class Restaurant(models.Model):
    name = models.CharField('Nome', max_length=150)
    email = models.EmailField('E-mail', max_length=150)
    phone = models.CharField('Telefone', max_length=14)
    name_restaurant = models.CharField('Nome do Restaurante', max_length=200)
    address = models.CharField('Endereço Restaurante', max_length=200)
    message = models.TextField('Messagem', null=True, blank=True)
    approved = models.BooleanField('Aprovado', default=False)
    date_register = models.DateTimeField('Registrado em', auto_now_add=True)

    
    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'

    def __str__(self):
        return self.name + ' - ' + self.name_restaurant