import requests


class Suap():
    def __init__(self):
        self.__endpoint = "https://suap.ifrn.edu.br/api/v2/"

    def autentica(self, username, password):
        ret = None

        url = self.__endpoint + "autenticacao/token/?format=json"

        headers = {'Content-type': 'application/json'}

        payload = '{"username": "%s", "password": "%s"}' % (username, password)

        result = requests.post(url, data=payload, headers=headers)

        if result.status_code == 200:

            data = result.json()

            if 'access' in data:
                ret = data['access']

        return ret

    def getMeusDados(self, token):
        ret = None

        url = self.__endpoint + "minhas-informacoes/meus-dados/"

        headers = {'Content-type': 'application/json',
                   'Authorization': 'Bearer %s' % token}

        payload = '{"token": "%s"}' % token

        result = requests.get(url, data=payload, headers=headers)

        if result.status_code == 200:

            data = result.json()

            if data is not None:
                ret = data

        return ret

    def execute(self, args: dict):

        ret = None

        if args is None or len(args) == 0:
            ret = '{"status": "error", "message": "Sem parâmetros necessários."}'
        else:
            url = self.__endpoint + args['method']

            headers = {'Content-type': 'application/json',
                       'Authorization': 'Bearer %s' % args['token']}

            payload = '{"token": "%s"}' % args['token']

            result = requests.get(url, data=payload, headers=headers)
            print(result)

            if result.status_code == 200:

                data = result.json()

                if data is not None:
                    ret = data

        return ret



