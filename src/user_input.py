from src.api import HH_API, SJ_API

from src.vacancy import Vacancy
from src.saver import JsonSaver


def main():
    #
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
            print('Введите название вакансии')
            keyword = input()
            hh_api = HH_API()
            hh_data = hh_api.get_vacancies(keyword)
            return hh_data
        elif user_input == 2:
            print('Введите название вакансии')
            keyword = input()
            sj_api = SJ_API()
            sj_data = sj_api.get_vacancies(keyword)
            return sj_data
        else:
            print('Нет возможности выполнить запрос')
