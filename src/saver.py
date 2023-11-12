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

    @abstractmethod
    def delete_vacancy(self, url, data):
        """Метод удаления вакансий"""
        pass


class JsonSaver(Saver):

    def load_file(self, filename='vacancies.json'):
         with open(file=filename, mode='r', encoding='utf-8') as file:
             return json.load(file)

    def save_file(self, data, filename='vacancies.json'):
        with open(file=filename, mode="w", encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

    def delete_vacancy(self, url, data):
        """Метод удаления вакансии"""
        for item in data:
            if item['url'] == url:
                data.remove(item)
        return data
