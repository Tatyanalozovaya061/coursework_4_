class Vacancy:
    """Класс для хранения информации о вакансии"""

    def __init__(self, name, url, salary_from, requirement):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.requirement = requirement

    def __str__(self):
        return f'Название вакансии - {self.name}\n' \
               f'Ссылка - {self.url}\n' \
               f'Зарплата - от {self.salary_from}\n' \
               f'Требования - {self.requirement}\n' \


    def to_dict(self):
        """Функция, представляющая вакансию в виде словаря"""
        return {
            'name': self.name,
            'url': self.url,
            'salary_from': self.salary_from,
            'description': self.requirement
        }

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
