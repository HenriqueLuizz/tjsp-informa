import os
import requests
import datetime
from bs4 import BeautifulSoup

def get_info():
    informes = []

    req = requests.get('https://tjsp.jus.br/Indisponibilidade/Comunicados')
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    # Utilizando somente o nome da tag HTML
    table = soup.find(name='div')
    # Especificando atributos da tag
    table = soup.find_all(name='div', attrs={'class':'lista-comunicados'})
    # Usando find_all
    # table = soup.find_all(name='div')
    for i in table:
        
        data = {
            "date": str(i.find(name='time').getText()).strip(), 
            "title": str(i.find(name='a').getText()).strip(), 
            "href": 'https://tjsp.jus.br/'+ str(i.find(name='a').get('href')).strip(), 
            "description": str(i.find(name='p').getText()).strip()
            }
        
        informes.append(data)

    print(f'Encontrei {len(informes)} comunidados do TJSP.')
    
    return informes


def bot_protheus(bot_message):

    bot_token = os.getenv('BOT_TOKEN',None)
    bot_chatID = os.getenv('BOT_CHATID',None)
    
    if bot_token is None and bot_chatID is None:
        print('Configure as chaves bot_token e bot_chatid')
        return
        
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    
    return response.json()

def bot_tjsp():

    infos = get_info()
    today = datetime.date.today()
    today = today.strftime("%d/%m/%Y")

    for msg in infos:
        date = msg.get('date')
        title = msg.get('title')
        href = msg.get('href')
        desc = msg.get('description')
        speak = f'Olá! \nTenho um recado do TJSP que foi publicado em {date}. \n\n{title} \n{desc} \n\nPara mais detalhes acesso o link {href} \n\nAté mais!'
        
        if date == today:
            print(speak)
            bot_protheus(speak)

    return { 'message': True}

if __name__ == "__main__":
    bot_tjsp()