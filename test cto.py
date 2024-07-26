
import re
from collections import Counter
import math

text = "the chiet technology officer (CTO) is na executive position in a company or other entity whose occupation is focused on scientific and technological issues within an organization. the CTO is very similar to a chiet technology officer (CTO). The CTO is the highest-ranking techonology executive within a company and leads the technology or engineering department. They develop policies and procedures and use technology to improve products and services that focus on external customers."

def limpar_texto(text):
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return texto_limpo
def AnalisarFrequencia(texto, n=3):
 texto_limpo = limpar_texto(texto)
 #textCase = re.findall("the",texto_limpo.lower())
 textMax = re.findall(r'\b\w+\b', texto_limpo.lower())
 contagem = Counter(textMax)
 mais_comuns = contagem.most_common(n)
 menos_comum = contagem.most_common()[-1]
 return mais_comuns, menos_comum

mais_comuns, menos_comum = AnalisarFrequencia(text)
print("Palavras mais comuns:")
for palavra, frequencia in mais_comuns:
    print(f'{palavra}: {frequencia}')
palavra_menos_comum, frequencia_menos_comum = menos_comum
print(f'\nPalavra menos comum: {palavra_menos_comum} com {frequencia_menos_comum} ocorrência(s)')


