import requests

from Coleta_Dados_Web import requisicao


def enviar_arquivo():

    #Caminho do arquivo para upload
    caminho = 'C:/Users/welly/PycharmProjects/ColetaDados/produtos_informatica.xlsx'

# Enviar o arquivo
    requisicao = requests.post('https://file.io/', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print('arquivo enviado. Link para acesso:', url)


def enviar_arquivo_chave():
    # Caminho do arquivo e chave para upload
    caminho = 'C:/Users/welly/PycharmProjects/ColetaDados/produtos_informatica.xlsx'
    chave_acesso = 'anslgme.aloskde-aldkejk-aksldeo-alskdke' # API KEY

    # Enviar o arquivo
    requisicao = requests.post(
    'https://www.file.io/',
        files={'file': open(caminho, 'rb')},
        readers={'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print('arquivo enviado com chave. Link para acesso:', url)

def receber_arquivo(file_url):
    # Receber arquivo
    requisicao = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso.')
    else:
        print('Erro ao baixar o arquivo.', requisicao.json())


#enviar_arquivo()
# enviar_arquivo_chave()
receber_arquivo('https://file.io/in3WfMrVFdt4')