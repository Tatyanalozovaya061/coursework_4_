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
    def remove_vacancy(self):
        """Метод удаления вакансий"""
        pass


class JsonSaver(Vacancy, Saver):

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        self.__all_vacancies = []

    def load_json(self):
        with open(self.data, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_json(self):
        with open(self.data, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy):
        """Метод добавления вакансий"""
        new_vacancy = {
            'name': vacancy.name,
            'url': vacancy.url,
            'area': vacancy.area,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'requirement': vacancy.requirement,
            'responsibility': vacancy.responsibility
        }
        data = list(self.load_json())
        data.append(new_vacancy)
        self.save_json(data)

    def sort_vacancies_by_salary(self):
        """Метод сортировки вакансий по зарплате"""
        self.__all_vacancies.sort(reverse=True)

    def get_data_from_a_file(self):
        """Метод получения данных из json-файла"""
        data = self.load_json()
        return data

    def remove_vacancy(self, id):
        data = self.load_json()
        for item in data:
            if item['id'] == id:
                data.remove(item)
        return data
