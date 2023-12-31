from abc import ABC, abstractmethod
import requests
from src.vacancy import Vacancy
import json


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    @abstractmethod
    def get_from_vacancy(self, vacancies):
        pass


class HH_API(API):

    def __init__(self, page=0, per_page=1):
        self.url = 'https://api.hh.ru/vacancies'
        self.page = page
        self.per_page = per_page

    def get_vacancies(self, keyword):
        params = {
            'text': keyword,
            'page': self.page,
            'count': self.per_page
        }
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()['items']

    def get_from_vacancy(self, vacancies):
        """Инициализация вакансий HH"""
        hh_vacancies = []
        for item in vacancies:
            name = item.get('name', 'Не найдено')
            url = item.get('alternate_url', 'Не найдено')
            salary_from = 0
            try:
                salary = item.get('salary', None)
                if salary is not None:
                    salary_from = salary['from']
                    if salary_from is None:
                        salary_from = 0
            except KeyError:
                pass
            try:
                requirement = item['snippet']['requirement']
            except KeyError or TypeError:
                requirement = 'Не найдено'
            vacancy = Vacancy(
                name=name,
                url=url,
                salary_from=salary_from,
                requirement=requirement,
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

    def get_from_vacancy(self, vacancies):
        """Инициализация вакансий SJ"""
        sj_vacancies = []
        for item in vacancies:
            name = item.get('profession', 'Не найдено')
            url = item.get('link', 'Не найдено')
            salary_from = item.get('payment_from', 0)
            requirement = item.get('vacancyRichText', 'Не найдено')
            vacancy = Vacancy(
                name=name,
                url=url,
                salary_from=salary_from,
                requirement=requirement,
            )
            sj_vacancies.append(vacancy)
        return sj_vacancies
