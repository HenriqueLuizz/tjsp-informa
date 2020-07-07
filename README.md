# tjsp-informa
Uma aplicação que busca as informações de indisponibilidade do TJSP e envia no Telegram

## CONFIGURAÇÃO

Para que as mesagens de indisponibilidade do TJSP sejam envaminhadas é necessário configurar as duas variáveis de ambiente *BOT_TOKEN* e *BOT_CHATID*.
É necessário que tenha um bot do Telegram, para mais informções de como criar um bot acesse o [link](https://core.telegram.org/bots#6-botfather)

Com o bot criado, é necessário que envie uma mensagem para ele e verifique o id do chat pela api do bot `https://api.telegram.org/bot{TOKEN_ID_DO_SEU_BOT}/getUpdates`

O retorno será semelhante ao json abaixo:

```json
{"ok":true,"result":[{"update_id":000000001, "message":{"message_id":2,"from":{"id":11111111, "is_bot":false,"first_name":"Fulano","last_name":"Silva","username":"FulanoSilva","language_code":"pt-br"},"chat":{"id":11111111,"first_name":"Fulano","last_name":"Silva","username":"FulanoSilva","type":"private"},"date":1591709046,"text":"oi"}}]}
```

Neste caso o id do chat é o `11111111`, este é o valor que será utilizado na variável de ambiente BOT_CHATID. `"chat":{"id":11111111,...`

Para exportar as variáveis de ambiente.

```sh
export BOT_TOKEN='TOKEN_ID_BOT_TELEGRAM'
export BOT_CHATID='ID_DO_CHAT'
```

## Executando o script

```sh
python bot_tjsp.py
```
