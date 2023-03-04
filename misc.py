import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        headears={ 'X-Api-key': api_key}
        r=requests.get(f'{self.get_url()}Misc/Cultures',headers=headears)
        return r.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        headers={ 'X-Api-Key': api_key }
        poylaud={ 
            'number': number,
            'culture': culture
                }
        r=requests.get(f'{self.get_url()}Misc/Random-Address', params=poylaud, headers=headers)
        return r.json()

ans=Misc()
key = "940a688e878544858234dee258149563"
print(ans.get_random_address(api_key=key, number=5))
print(ans.get_cultures(key))
