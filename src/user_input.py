from src.api import HH_API, SJ_API

from src.saver import JsonSaver
from pprint import pprint


def main():

    while True:
        user_input = input('Выберите платформу:\n'
                           '1 - HeadHanter\n'
                           '2 - SuperJob\n'
                           '0 - Exit\n'
                           'Ввод пользователя: '
        )

        if user_input == "0":
            break
        elif user_input == "1":
            print('Введите название вакансии: ')
            keyword = input()
            hh_api = HH_API()
            hh_data = hh_api.get_vacancies(keyword)
            hh_data_ = hh_api.get_from_vacancy(hh_data)
            vacancies = []
            for item in hh_data_:
                pprint(item.to_dict(), sort_dicts=False)
                print()
                vacancies.append(item.to_dict())
            edit_file(vacancies)

        elif user_input == "2":
            print('Введите название вакансии')
            keyword = input()
            sj_api = SJ_API()
            sj_data = sj_api.get_vacancies(keyword)
            sj_data_ = sj_api.get_from_vacancy(sj_data)
            vacancies = []
            for item in sj_data_:
                pprint(item.to_dict(), sort_dicts=False)
                print()
                vacancies.append(item.to_dict())
            edit_file(vacancies)
        else:
            print('Нет возможности выполнить запрос')
            exit()


def edit_file(vacancies):
    """Интерфейс сохранения полученных данных с сортировкой и удаления"""
    user_input = input('Редактируем данные (сортировка, удаление) перед сохранением списка вакансий? \n'
                 '1 - сортировка по ЗП\n'
                 '2 - удаление вакансии\n'
                 '3 - сохранение в файл без редактирования\n'
                 '0 - Exit\n'
                 'Ввод пользователя: '
    )
    if user_input == "1":
        salary_sort = sorted(vacancies, key=lambda x: x["salary_from"])
        json_saver = JsonSaver()
        json_saver.save_file(salary_sort)
        print("Файл сохранен")
    elif user_input == "2":
        url = input("Введите url из списка для удаления позиции: ")
        json_saver = JsonSaver()
        data = json_saver.delete_vacancy(url, vacancies)
        json_saver.save_file(data)
        print("Файл сохранен")
    elif user_input == "3":
        json_saver = JsonSaver()
        json_saver.save_file(vacancies)
        print("Файл сохранен")
    elif user_input == "0":
        exit()
    else:
        print('Нет возможности выполнить запрос')
        exit()


if __name__ == '__main__':
    main()
