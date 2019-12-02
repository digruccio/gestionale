# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Cliente, Fattura, Prodotto

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Fattura)
admin.site.register(Prodotto)

