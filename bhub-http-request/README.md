# BHUB Challenge - Lambda de exemplo (requisição HTTP)

## Aplicação desenvolvida em [Chalice](https://aws.github.io/chalice/) para ler as mensagens da fila bhub-http do SQS e enviar o json para a url que vem configurada no mesmo JSON, juntamente com os demais parâmetros.

## Como testar e realizar deploy:

1. Criar ambiente virtual (atualmente o Lambda suporta o Python 3.11): `python -m venv .venv`

2. Ativar o ambiente virtual: 

  - Linux: `source .venv/bin/activate`

  - Windows cmd: `.venv\Scripts\activate.bat`

  - Windows Powershell: `.venv\Scripts\Activate.ps1`

3. Instalar dependências: `pip install -r requirements.txt`

4. Para realizar o deploy, você precisa instalar o chalice e o boto3: `pip install chalice boto3`

5. Comando de deploy: `chalice deploy --stage=prod`
