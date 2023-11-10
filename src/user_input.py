from src.api import HH_API, SJ_API

from src.vacancy import Vacancy
from src.saver import JsonSaver


# def main():
#
#     # hh_api = HH_API()
#     # sj_api = SJ_API()
#
#     while True:
#         user_input = input('Выберите платформу:\n'
#             '1 - HeadHanter\n'
#             '2 - SuperJob\n'
#             '0 - Exit'
#         )
#         if user_input == 0:
#             break
#         elif user_input == 1:
#             print('Введите название вакансии')
#             keyword = input()
#             hh_api = HH_API()
#             hh_data = hh_api.get_vacancies(keyword)
#             return hh_data
#         elif user_input == 2:
#             print('Введите название вакансии')
#             keyword = input()
#             sj_api = SJ_API()
#             sj_data = sj_api.get_vacancies(keyword)
#             return sj_data
#         else:
#             print('Нет возможности выполнить запрос')

def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ")
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
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


