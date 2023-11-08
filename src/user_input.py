from src.api import HH_API, SJ_API

from src.vacancy import Vacancy
from src.saver import JsonSaver


def main():

    # hh_api = HH_API()
    # sj_api = SJ_API()

    while True:
        user_input = input('Выберите платформу:\n'
            '1 - HeadHanter\n'
            '2 - SuperJob\n'
            '0 - Exit'
        )
        if user_input == 0:
            break
        elif user_input == 1:
            user_input = input('Введите название вакансии')
            hh_api = HH_API(user_input)
            hh_data = hh_api.get_vacancies()
            print(hh_data)
