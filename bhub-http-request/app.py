import json

import httpx
from chalice import Chalice


# variaveis
QUEUE_NAME = 'bhub-http'

# Chalice
app = Chalice(app_name=f'{QUEUE_NAME}-lambda')
app.debug = True


@app.on_sqs_message(queue=f'{QUEUE_NAME}')
def handle_sqs_message(event):
    for item in event:
        config = json.loads(item.body)
        body = {**config['product'], **config['order']}
        res = httpx.request(
            method=config['method'],
            url=config['url'],
            json=body,
            params=config['params'],
            headers=config['headers'],
        )
    if res.is_error:
        app.log.debug(
            f'Error sending HTTP request with following config: {config}'
        )
    app.log.debug(res.json())
