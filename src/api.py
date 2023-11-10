from abc import ABC, abstractmethod
import requests
from src.vacancy import Vacancy
import json


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_from_vacancy(self):
        pass


class HH_API(API):

    def __init__(self, page=0, per_page=1):
        self.url = 'https://api.hh.ru/vacancies'
        self.page = page
        self.per_page = per_page

    def get_vacancies(self, keyword):
        params = {
            'keyword': keyword,
            'page': self.page,
            'count': self.per_page
        }
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()['items']

    # def __init__(self, keyword):
    #     self.url = 'https://api.hh.ru/vacancies'
    #     self.params = {
    #         'text': keyword,
    #         'per_page': 10,
    #         'area': 76,
    #     }

    # def get_vacancies(self):
    #     response = requests.get(self.url, params=self.params)
    #     return response.json()['items']

    def get_from_vacancy(self, vacancies):
        """Инициализация вакансий"""
        hh_vacancies = []
        for item in vacancies:
            if item['name'] == 'RUR':
                vacancy = Vacancy(
                    item['name'],
                    item['alternate_url'],
                    item['area']['name'],
                    item['salary']['from'],
                    item['salary']['to'],
                    item['snippet']['requirement'],
                    item['snippet']['responsibility']
                )
                hh_vacancies.append(vacancy)
            return hh_vacancies


class SJ_API(API):

    def __init__(self, page=0, per_page=1):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.page = page
        self.per_page = per_page

    def get_vacancies(self, keyword):
        headers = {
            'X-Api-App-Id': 'v3.r.137938026.472091ca7ace53501414d05230270f9e1007e789.'
                            '50cde4769f3f555625a49678669cd3b827f2e7f0'
        }
        params = {
            'keyword': keyword,
            'page': self.page,
            'count': self.per_page
        }
        response = requests.get(self.url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()['objects']

    def get_from_vacancy(self):
        pass


# if __name__ == '__main__':
#     hh_api = HH_API()
#     print(hh_api.get_from_vacancy())