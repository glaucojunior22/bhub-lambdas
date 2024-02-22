# BHUB Challenge - Lambda de exemplo (Envio de E-mails)

## Aplicação desenvolvida em [Chalice](https://aws.github.io/chalice/) para ler as mensagens da fila bhub-email do SQS e enviar um e-mail para um usuário utilizando os dados do JSON.

## Como testar e realizar deploy:

1. Criar ambiente virtual (atualmente o Lambda suporta o Python 3.11): `python -m venv .venv`

2. Ativar o ambiente virtual: 

  - Linux: `source .venv/bin/activate`

  - Windows cmd: `.venv\Scripts\activate.bat`

  - Windows Powershell: `.venv\Scripts\Activate.ps1`

3. Instalar dependências: `pip install -r requirements.txt`

4. Para realizar o deploy, você precisa instalar o chalice e o boto3: `pip install chalice boto3`

5. Configure as variáveis de ambiente com as credenciais do servidor de e-mail, o arquivo se encontra em `.chalice/config.json`
   As variáveis necessárias são: EMAIL_HOST, EMAIL_USER, EMAIL_PASS, EMAIL_PORT
   
6. Comando de deploy: `chalice deploy --stage=prod`
