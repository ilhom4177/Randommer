import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        url = self.base_url + 'Card'
        payload = {
            "type": type
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params=payload, headers=headers)

        return response.json()

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        url = self.get_url() + 'Card/Types'
        headers = {'X-Api-Key': api_key}
        response = requests.get(url, headers=headers)
        return response.json()

card = Card()
print(card.get_card_types("2d794c6f46094ceb96bd719c1c26c984"))