# -*- coding: utf-8 -*-

from tutorinteligente.models import *

from django.contrib.auth import *

from social_auth.models import *

class Aluno:

    def acao(self, percepcao, estudante):
        if percepcao == 'informar_nivel_estudante':
            return self.procurar_nivel_estudante(estudante)

        if percepcao == 'informar_estado_estudante':
            return self.procurar_estado_estudante(estudante)

        if percepcao == 'informar_dados_estudante':
            return self.procurar_dados_estudante(estudante)


    def procurar_nivel_estudante(self, estudante):
        nivel_estudante = Estudante.objects.filter(fb_id = estudante).values_list('escolaridade', flat=True)
        #nivel_estudante = nivel_estudante.values('escolaridade')
        return nivel_estudante[0]

    def procurar_estado_estudante(self, estudante):
        estado_estudante = Estudante.objects.filter(fb_id = estudante)
        estado_estudante = estado_estudante.values_list('fk_id_estudante_estado__nome', flat=True)
        return estado_estudante[0]

    def procurar_dados_estudante(self, estudante):
        nome_estudante = Estudante.objects.filter(fb_id = estudante).values_list('fk_id_estudante_estado__nome', flat=True)

        if not nome_estudante:
            user_id_social = UserSocialAuth.objects.filter(uid = estudante).values_list('user_id__username', flat=True)
            django_user = user_id_social[0]

            estado_estudante = Estudante_Estado.objects.get(nome='Neutro')
            novo_estudante = Estudante(fb_id=estudante ,nome=django_user, escolaridade='Medio', qi=0, fk_id_estudante_estado=estado_estudante)
            novo_estudante.save()

            dados_estudante = Estudante.objects.filter(fb_id = estudante)
        else:
            dados_estudante = Estudante.objects.filter(fb_id = estudante)

        return dados_estudante


