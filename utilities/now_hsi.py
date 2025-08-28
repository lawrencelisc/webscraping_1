import requests


class index_data:
    def __init__(self):
        self.headers = {
            'Accept-Language': 'text/html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
        }
        self.base_url = 'https://finance.now.com/api/getAfeQuote.php'
        self.params = {
            'item': 'allindex'
        }

    def get_update(self, ref_ts: int) -> list:
        index_data = []
        req = requests.get(url=self.base_url, params=self.params, headers=self.headers)

        if req.status_code != 200:
            return index_data

        j = req.json()
        index_list = j.get('indexInfos')

        if index_list is not None:
            for fnl in index_list:
                code = fnl['code']
                sysdate = fnl['sysdate']
                index = str(fnl['index'])
                volume = str(fnl['volume'])
                index_data.append({
                    'code': code,
                    'sysdate': sysdate,
                    'index': index,
                    'volume': volume
                })

        return index_data