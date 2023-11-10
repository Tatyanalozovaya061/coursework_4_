class Vacancy:
    """Класс для хранения информации о вакансии"""

    def __init__(self, name, url, area, salary_from, salary_to, requirement, responsibility):
        self.name = name
        self.url = url
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement
        self.responsibility = responsibility
        # self.currency = 'RUR'

    def __str__(self):
        return f'Название вакансии - {self.name}\n' \
               f'Ссылка - {self.url}\n' \
               f'Город - {self.area}\n' \
               f'Зарплата - от {self.salary_from} до {self.salary_to}\n' \
               f'Требования - {self.requirement}\n' \
               f'Описание - {self.responsibility}\n' \


    # def to_dict(self):
    #     """Функция, представляющая вакансию в виде словаря"""
    #     return {
    #         'name': self.name,
    #         'url': self.url,
    #         'salary_from': self.salary_from,
    #         'salary_to': self.salary_to,
    #         'description': self.description
    #     }

    # def __lt__(self, other):
    #     return self.salary_from < other.salary_from
    #
    # def __le__(self, other):
    #     return self.salary_from <= other.salary_from
    #
    # def __eq__(self, other):
    #     return self.salary_from == other.salary_from
    #
    # def __ne__(self, other):
    #     return self.salary_from != other.salary_from


# class Vacancies:
#     """Класс хранения и обработки вакансий"""
#
#     def __init__(self):
#         self.__all_vacancies = []

    # def add_vacancies(self, new_vacancies):
    #     """Метод добавления вакансий"""
    #     self._all_vacancies += new_vacancies

    # def sort_vacancies_by_salary(self):
    #     """Метод сортировки вакансий по зарплате"""
    #     self._all_vacancies.sort(reverse=True)

    # @property
    # def all_vacancies(self):
    #     """Метод получения всех вакансий"""
    #     return self._all_vacancies
    #
    # def to_list_dict(self):
    #     """Метод перевода вакансий в список словарей"""
    #     list_vac = []
    #     for item in self._all_vacancies:
    #         list_vac.append(item.to_dict())
    #     return list_vac
