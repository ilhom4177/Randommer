import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        headers={ 'X-Api-Key':api_key}
        poyloud={  'nameType': nameType,
                    'quantity': quantity,
                }
        r=requests.get(f'{self.get_url()}Name', params=poyloud , headers=headers )
        return r.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        headers={ 'X-Api-Key': api_key}
        params={'startingWords' : startingWords }
        r=requests.get(f'{self.get_url()}Name/Suggestions',headers=headers,params=params)
        return r.json()
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        headers={ 'X-Api-Key': api_key}
        r=requests.get(f'{self.get_url()}Name/Cultures',headers=headers)
        return r.json()




ans=Name()
key = "940a688e878544858234dee258149563"
print(ans.get_name(key,'fullname',5))
print(ans.get_name_suggestions(key,'hello'))
print(ans.get_name_cultures(key))