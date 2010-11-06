# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from random import choice
import string

ESPECIALES = u'¿"&$%/\]{}(=?)*@!-_¡+^['
SIZE = 20
PWDS = 10
HARD = True

def index(request):
    lista = []
    for i in range(PWDS):
        clave = ''.join(choice(u''+string.letters + u''+string.digits + ESPECIALES) for _ in range(SIZE))
        lista.append(clave)
    print lista
    return render_to_response('index.html', RequestContext(request, locals()))

