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
        if type is not None:
            payload = {
                "type": type
            }
            headers = {
                "X-Api-Key": api_key
            }
            response = requests.get(url, params=payload, headers=headers)
        else:
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
        url = self.base_url+'Card/Types'
        headers = {
            "X-Api-Key":api_key
        }
       
        r = requests.get(url, headers=headers)
        return r.json()

card = Card()
key = "940a688e878544858234dee258149563"

print(card.get_card_types(key))