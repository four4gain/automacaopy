import requests
from bs4 import BeautifulSoup
import pandas as pd

def extrair_dados_categoria(url, categoria):
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f'Sucesso ao acessar a URL {url}')
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        dados_da_pagina = soup.find_all('p')


        for dado in dados_da_pagina:
            dados.append({'Categoria': categoria, 'Dado': dado.get_text()})
    else:
        print(f'Erro ao acessar a URL {url}: {response.status_code}')


base_url = 'https://silviaestima.com.br/'


categorias = [
    ('aliancas/bodas', 2),
    ('aliancas/classicas', 3),
    ('aliancas/desenhadas', 4),
    ('aliancas/pares', 1),
    ('infantil/brincos', 2),
    ('infantil/pulseiras', 1),
]

dados = []


for categoria, num_page in categorias:
    if num_page == 1:
     
        url = f'{base_url}/product-category/{categoria.lower()}/'
        extrair_dados_categoria(url, categoria)
    elif num_page > 1:
    
        for page in range(1, num_page + 1):
            url = f'{base_url}/product-category/{categoria.lower()}/page/{page}/'
            extrair_dados_categoria(url, categoria)


df = pd.DataFrame(dados)


df.to_excel('joias.xlsx', index=False)

print('Dados extraídos e salvos em dados.xlsx')


#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 
#ME ARRUMA UM ESTÁGIO AI!! 






