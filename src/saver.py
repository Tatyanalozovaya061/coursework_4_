from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy


class Saver(ABC):

    @abstractmethod
    def load_file(self, filename):
        pass

    @abstractmethod
    def save_file(self, data, filename):
        pass
    #
    # @abstractmethod
    # def add_vacancy(self):
    #     pass
    #
    # @abstractmethod
    # def get_data_from_a_file(self):
    #     pass
    #
    # @abstractmethod
    # def get_vacancies_by_salary(self):
    #     pass
    #
    # @abstractmethod
    # def delete_vacancy(self):
    #     """Метод удаления вакансий"""
    #     pass


class JsonSaver(Saver):

    def load_file(self, filename='vacancies.json'):
         with open(file=filename, mode='r', encoding='utf-8') as file:
             return json.load(file)

    def save_file(self, data, filename='vacancies.json'):
        with open(file=filename, mode="w", encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
