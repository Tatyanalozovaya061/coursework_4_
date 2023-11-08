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
    def get_from_hh(self):
        pass


class HH_API(API):

    def __init__(self, keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'text': keyword,
            'per_page': 10,
            'area': 76,
        }

    def get_vacancies(self):
        response = requests.get(self.url, params=self.params)
        return response.json()['items']

    def get_from_hh(self, vacancies):
        """Инициализация вакансий"""
        vacancies_list = []
        for item in vacancies:
            if item['salary']['currency'] == 'RUR':
                vacancy = Vacancy(
                    item['name'],
                    item['alternate_url'],
                    item['area']['name'],
                    item['salary']['from'],
                    item['salary']['to'],
                    item['snippet']['requirement'],
                    item['snippet']['responsibility']
                )
                vacancies_list.append(vacancy)
            return vacancies_list


class SJ_API(API):

    def __init__(self, keyword):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.params = {
            'keyword': keyword,
            'count': 10,
            'town': 113
        }

    def get_vacancies(self):
        headers = {
            'X-Api-App-Id': 'v3.r.137938026.472091ca7ace53501414d05230270f9e1007e789.50cde4769f3f555625a49678669cd3b827f2e7f0'
        }
        response = requests.get(self.url, headers=headers, params=self.params)
        vacancies = response.json()['objects']
