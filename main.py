# type: ignore
import requests
import time
import dotenv


# Carregando as variáveis de ambiente
dotenv.load_dotenv()


"""
Passar o token do bot diretamente no código não é uma boa prática.
Mas para fins didáticos, você pode passar o token diretamente, somente dessa vez hein ;)
"""
BOT_TOKEN = "SEU_TOKEN"


"""
Url da API do telegram
"""
API_URL = "https://api.telegram.org/bot" + BOT_TOKEN


def pegar_atualizacoes(offset=None):
    """
    Pegando as atualizações através da api
    Offset é um "id" que indica a partir de qual mensagem você quer pegar as atualizações.
    Por exemplo, se você passar o offset 10, você vai pegar as mensagens a partir da 11ª.

    A maneira mais fácil de pegar as atualizações, é ficar perguntando para a api se tem novas atualizações.
    E é isso que a nossa função faz
    """

    url = API_URL + "/getUpdates"
    params = {"offset": offset}

    time.sleep(5)  # Espera 5 segundos antes de fazer a próxima requisição

    resposta = requests.get(url, params=params)
    return resposta.json()


def enviar_mensagem(chat_id, mensagem):
    """
    Envia a mensagem ao chat especificado
    """

    url = API_URL + "/sendMessage"
    params = {"chat_id": chat_id, "text": mensagem}
    requests.post(url, params=params)


def rodar_bot():
    """
    Roda o bot até pararmos ele
    """

    offset = None
    print("Rodando bot")
    while True:
        atualizacoes = pegar_atualizacoes(offset)
        for atualizacao in atualizacoes["result"]:
            mensagem = atualizacao["message"]["text"]
            chat_id = atualizacao["message"]["chat"]["id"]

            if mensagem == "/start":
                enviar_mensagem(chat_id, "Olá, eu sou um BorbaBot!")

            offset = atualizacao["update_id"] + 1


rodar_bot()
