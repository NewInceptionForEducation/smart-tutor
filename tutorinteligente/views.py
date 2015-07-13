# Create your views here.
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotModified
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from tutorinteligente.agentes.tutor import *

import urllib2
import json
import pdb

# Ambiente
@login_required
def ambiente(request):
	#pdb.set_trace()
	estudante = request.user.username

	url_perfil_estudante = 'https://graph.facebook.com/' + estudante
	resp_perfil_estudante = urllib2.urlopen(url_perfil_estudante).read()
	perfil_estudante = json.loads(resp_perfil_estudante.decode('utf-8'))

	nome_estudante = perfil_estudante['name']
	id_estudante = perfil_estudante['id']

	url_foto_estudante = 'https://graph.facebook.com/' + id_estudante + '/picture?type=large'
	foto_estudante = url_foto_estudante

	tutor = Tutor()
	dados_estudante = tutor.acao(percepcao='estudante_entrou', estudante=id_estudante)
	print dir(dados_estudante)

	if request.POST:
		if not request.POST['pergunta']:
			return HttpResponseNotModified()
		else:
			tutor = Tutor()
			pergunta = request.POST['pergunta']
			resposta = tutor.acao('estudante_perguntou', id_estudante, pergunta)
			print dir(resposta)
			return render_to_response('index.html',{
				'nome_estudante': nome_estudante,
				'foto_estudante': foto_estudante,
				'dados_estudante': dados_estudante,
				'resposta': resposta
			},
			context_instance=RequestContext(request))
	else:
		return render_to_response('index.html',{
			'nome_estudante': nome_estudante,
			'foto_estudante': foto_estudante,
			'dados_estudante': dados_estudante
		},
	    context_instance=RequestContext(request))
