from enum import auto
from django.db import models
from cpf_field.models import CPFField
from django.forms import EmailField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Cadastro(models.Model):
    ANO_CHOICES = [
         (1, '2021'),
         (2, '2022'),
         (3, '2023'),
         (4, '2024'),
                ]
    CONDICAO_CHOICES =  [
         (1,  'Em aberto'), 
         (2,  'Pago'),
         (3,    'Julho a dezembro' ),
         (3,  'Ate janeiro'),
         (4,  'Ate fevereiro'),
         (5,  'Ate março'),
         (6,  'Ate abril'),
         (7,  'Ate maio'),
         (8,  'Ate junho'),
         (9,  'Ate julho'),
         (10, 'Ate agosto'),
         (11, 'Ate setembro'),
         (12, 'Ate outubro'),
         (13, 'Ate novembro'),
         (14, 'Ate dezembro'),
    ]   
    TPCIO_CHOICES = [
      (1, '1-PATRIM'),
      (2, '2-CONTRIB'),
    ]
    
    nome = models.CharField('Nome do Socio', max_length=250)
  #  club = models.IntegerField('Tipo socio', default='1-PATRIM', choices=TPCIO_CHOICES)
  #   cpf = models.CharField('CPF do socio', max_length=250, blank=True, null=True)
    cpf = CPFField('CPF do socio',  blank=True, null=True)
    valor=models.DecimalField(verbose_name='Valor em R$', max_digits=6, decimal_places=2, default=0, null=True, blank=True)
    ano_pago = models.IntegerField('Ano pagto', choices=ANO_CHOICES)
    condicao_pago = models.IntegerField('Status pagto', choices=CONDICAO_CHOICES)
    data_pago = models.DateField('Data pagamento', null=True, blank=True)
    observ = models.TextField('Observações', max_length=150, default='Mensalidades isentas 2020,2021 e 2022', blank=True)
 #   celular = models.CharField('Núm. celular', max_length=25)
    celular = PhoneNumberField('Núm. celular')
    data_nascimento = models.DateField('Data Nascimento', null=True, blank=True)
    email = models.EmailField(verbose_name=u'E-mail', max_length=50, null=True, blank=True)
   

   

    def __str__(self):
           return str(self.nome)

    class Meta:
         verbose_name = 'Sócio cadastrado'
         verbose_name_plural = 'Sócios cadastrados'