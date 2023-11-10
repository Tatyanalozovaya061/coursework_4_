from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy


class Saver(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_data_from_a_file(self):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Метод удаления вакансий"""
        pass


class JsonSaver(Vacancy, Saver):

    def __init__(self, data):
        pass
        # super().__init__(data)
        self.data = data
        # self.__all_vacancies = []

    def load_json(self):
        with open(self.data, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_json(self):
        # with open(self.data, 'w', encoding='utf-8') as file:
        #     json.dump(self.data, file, indent=4, ensure_ascii=False)

        with open('vacancies.json', "w", encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False)


    def add_vacancy(self, vacancies):
        """Метод добавления вакансий в Json"""
        list_vacancy = []
        for vacancy in vacancies:
            new_vacancy = {
                'name': vacancy.name,
                'url': vacancy.url,
                'salary_from': vacancy.salary_from,
                'requirement': vacancy.requirement,
            }
            list_vacancy.append(new_vacancy)
        return list_vacancy


    def get_vacancies_by_salary(self):
        """Метод сортировки вакансий по зарплате"""
        self.__all_vacancies.sort(reverse=True)

    def get_data_from_a_file(self):
        """Метод получения данных из json-файла"""
        data = self.load_json()
        return data

    def delete_vacancy(self, id):
        data = self.load_json()
        for item in data:
            if item['id'] == id:
                data.remove(item)
        return data
