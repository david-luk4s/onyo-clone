from django.db import models


class Contact(models.Model):
    name = models.CharField('Nome', max_length=150)
    email = models.EmailField('E-mail', max_length=150)
    assunto = models.CharField('Assunto', max_length=250, null=True, blank=True)
    message = models.TextField('Messagem', max_length=600, null=True, blank=True)
    date_register = models.DateTimeField('Registrado em', auto_now_add=True)


    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.email + ' - ' + self.assunto