from src.api import HH_API, SJ_API
from pprint import pprint
from src.vacancy import Vacancies


from src.saver import *

if __name__ == '__main__':

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HH_API()
    # sj_api = SJ_API()

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies("Python")
    # sj_vacancies = sj_api.get_vacancies("Python")
    hh_v = hh_api.get_from_vacancy(hh_vacancies)
    # sj_v = sj_api.get_from_vacancy(sj_vacancies)
    vacancies = Vacancies()
    vacancies.add_vacancies(hh_v)
    # vacancies.add_vacancies(sj_v)
    # pprint(hh_api.get_vacancies("Python"))
    # vacancies.sort_vacancies_by_salary()
    j_list = vacancies.to_list_dict()
    s_json = JsonSaver()
    s_json.save_file(data=j_list, filename='test.json')
    new_list = s_json.load_file(filename='test.json')
    # vacancies = Vacancies()
    # vacancies.vacancy_from_list(new_list)
    # vacancies.print_vacancy(1)
    pprint(hh_api.get_vacancies("Python"))
