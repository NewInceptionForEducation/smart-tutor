# -*- coding: utf-8 -*-

from tutorinteligente.models import *

from tutorinteligente.agentes.aluno import *
from tutorinteligente.agentes.dominio import *

class Tutor(object):

    def acao(self, percepcao, estudante, pergunta=None):
    	if percepcao == 'estudante_perguntou':
            resposta = self.responder_pergunta_estudante(pergunta, estudante)
            return resposta

        if percepcao == 'estudante_entrou':
            retorno = self.verificar_dados_estudante(estudante)
            return retorno


        #if percepcao == 'estudante_avaliou_resposta':
        #    if avaliacao_resposta == 'positiva':
        #        pass
        #    elif feedback_resposta == 'negativa':
        #        pass

    	#if percepcao == 'estudante_respondeu_pergunta':
    	#	if resposta == 'correta':
    	#		pass

    	#	elif resposta == 'errada':
    	#		pass

    def responder_pergunta_estudante(self, pergunta, estudante):
        aluno = Aluno()
        nivel_estudante = aluno.acao('informar_nivel_estudante', estudante)
        estado_estudante = aluno.acao('informar_estado_estudante', estudante)
        #regra_pedagogica = Regra_Redagogica.objects.filter()

        if estado_estudante == "Nao_Aprendendo":
            pass
        elif estado_estudante == "Aprendendo":
            if nivel_estudante == "Medio":
                nivel_objeto_ensino = 1
                dominio = Dominio()
                objeto_ensino = dominio.acao('enviar_objeto_ensino', pergunta, nivel_objeto_ensino)
                #objeto_ensino = 'erro 1'
                return objeto_ensino

            if nivel_estudante == "Superior":
                nivel_objeto_ensino = 1
                dominio = Dominio()
                objeto_ensino = dominio.acao('enviar_objeto_ensino', pergunta, nivel_objeto_ensino)
                #objeto_ensino = 'erro 2'
                return objeto_ensino
        else:
            pass

    def verificar_dados_estudante(self, estudante):
        aluno = Aluno()
        dados_estudante = aluno.acao('informar_dados_estudante', estudante)

        return dados_estudante