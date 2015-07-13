from django.db import models

# Create your models here.

#class User(models.Model):
#    """User Model Class"""
#    id = models.StringProperty(required=True) #facebook user-id
#    created = models.DateTimeProperty(auto_now_add=True)
#    updated = models.DateTimeProperty(auto_now=True)
#    name = models.StringProperty(required=True)
#    profile_url = models.StringProperty(required=True)
#    access_token = models.StringProperty(required=True)  #fb OAUTH access token

class Estudante_Estado(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=20, verbose_name='Nome')
	descricao = models.TextField(verbose_name='Descricao', blank=True, null=True)
	def __unicode__(self):
		return self.id
	class Meta:
		db_table = u'sti_estudante_estado'
		verbose_name = 'Estado Estudante'
		verbose_name_plural = 'Estado Estudantes'
		ordering = ['nome']


class Estudante(models.Model):
    id = models.AutoField(primary_key=True)
    fb_id = models.CharField(max_length=50, verbose_name='Facebook_id')
    nome = models.CharField(max_length=50, verbose_name='Nome')
    escolaridade = models.CharField(max_length=100, verbose_name='Escolaridade')
    qi = models.IntegerField(verbose_name='QI')
    fk_id_estudante_estado = models.ForeignKey(Estudante_Estado, db_column='fk_id_estudante_estado', verbose_name='Estado Estudante')
    def __unicode__(self):
        return self.fb_id
    class Meta:
        db_table = u'sti_estudante'
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'
        ordering = ['nome']


class Objeto_Ensino(models.Model):
	id = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=100, verbose_name='Titulo', blank=True, null=True)
	introducao = models.TextField(verbose_name='Intruducao', blank=True, null=True)
	conteudo = models.TextField(verbose_name='Conteudo', blank=True, null=True)
	tags = models.TextField(verbose_name='Tags', blank=True, null=True)
	nivel = models.IntegerField(max_length=1, verbose_name='Nivel')
	def __unicode__(self):
		return self.titulo
	class Meta:
		db_table = u'bdc_objeto_de_ensino'
		verbose_name = 'Objeto de Ensino'
		verbose_name_plural = 'Objetos de Ensino'
		ordering = ['titulo']