import csv
from datetime import datetime

class Pesquisa:
    def __init__(self):
        self.perguntas = [
            '1. Você já considerou contratar um seguro para o seu celular?',
            '2. Você decidiu não contratar um seguro de celular?',
            '3. Você acredita que o custo do seguro de celular é um fator importante na decisão de não contratá-lo?',
            '4. Você confia na capacidade das seguradoras de pagar em caso de necessidade?',
            '5. Você acha que os riscos de danos ou perda do celular são baixos o suficiente para não justificar a compra de um seguro?',
            '6. Você já teve experiências negativas com seguradoras que influenciaram sua decisão de não contratar um seguro de celular?',
            '7. Você acredita que a cobertura oferecida pelos seguros de celular é suficiente para suas necessidades?',
            '8. Você já considerou outras formas de proteger seu celular além de um seguro, como capas protetoras ou programas de garantia estendida?',
            '9. Se os seguros de celular oferecessem preços mais acessíveis ou benefícios adicionais, você reconsideraria contratar um seguro para o seu celular?'
        ]