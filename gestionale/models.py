# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Cliente(models.Model):
    ragioneSociale=models.CharField(max_length=100, null=True, db_index=True)
    piva=models.CharField(max_length=100, null=True)
    indirizzo=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.ragioneSociale

    def get_piva(self):
        return self.piva
    get_piva.short_description = "P.Iva"

#class ClienteAdmin(admin.ModelAdmin):
 #   list_display = ['cliente', 'get_piva']
    #search_fields = ['cliente', 'cliente__piva']
    


class Fattura(models.Model):
    codice=models.CharField(max_length=100, null=True)
    cliente=models.ForeignKey('Cliente')
    Prodotto=models.ManyToManyField('Prodotto') 
    data=models.DateField(null=True)

    def __unicode__(self):
        return self.codice


class Prodotto(models.Model):
    nome=models.CharField(max_length=100, null=True)
    prezzo=models.CharField(max_length=100, null=True)
    

    def __unicode__(self):
        return self.nome