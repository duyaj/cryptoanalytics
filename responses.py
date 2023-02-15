import requests

def handle_response(message) -> str:
        p_message = message.lower()

        if p_message == 'eth':
            url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'btc':
            url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'bnb':
            url = 'https://rest.coinapi.io/v1/exchangerate/BNB/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'xrp':
            url = 'https://rest.coinapi.io/v1/exchangerate/XRP/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'ada':
            url = 'https://rest.coinapi.io/v1/exchangerate/ADA/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'doge':
            url = 'https://rest.coinapi.io/v1/exchangerate/DOGE/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'matic':
            url = 'https://rest.coinapi.io/v1/exchangerate/MATIC/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'sol':
            url = 'https://rest.coinapi.io/v1/exchangerate/SOL/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'dot':
            url = 'https://rest.coinapi.io/v1/exchangerate/DOT/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'shib':
            url = 'https://rest.coinapi.io/v1/exchangerate/SHIB/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'ltc':
            url = 'https://rest.coinapi.io/v1/exchangerate/LTC/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'trx':
            url = 'https://rest.coinapi.io/v1/exchangerate/TRX/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'avax':
            url = 'https://rest.coinapi.io/v1/exchangerate/AVAX/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'uni':
            url = 'https://rest.coinapi.io/v1/exchangerate/UNI/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'atom':
            url = 'https://rest.coinapi.io/v1/exchangerate/ATOM/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'link':
            url = 'https://rest.coinapi.io/v1/exchangerate/LINK/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'leo':
            url = 'https://rest.coinapi.io/v1/exchangerate/LEO/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'xmr':
            url = 'https://rest.coinapi.io/v1/exchangerate/XMR/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'ton':
            url = 'https://rest.coinapi.io/v1/exchangerate/TON/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'okb':
            url = 'https://rest.coinapi.io/v1/exchangerate/OKB/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'apt':
            url = 'https://rest.coinapi.io/v1/exchangerate/APT/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"

        if p_message == 'xlm':
            url = 'https://rest.coinapi.io/v1/exchangerate/XLM/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return f"Based on my research, {response.get('asset_id_base')} is currently " \
                   f"trading at ${response.get('rate')}"