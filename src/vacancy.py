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


class Vacancies:
    """Класс хранения и обработки вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        """Метод добавления вакансий"""
        self.__all_vacancies.extend(new_vacancies)

    def sort_vacancies_by_salary(self, reverse=True):
        """Метод сортировки вакансий по зарплате"""
        # self.__all_vacancies.sort(reverse=True)
        proceed_vacancies = sorted(self.__all_vacancies, key=lambda x: x.salary_from, reverse=reverse)
        self.__all_vacancies = proceed_vacancies

    @property
    def all_vacancies(self):
        """Метод получения всех вакансий"""
        return self.__all_vacancies

    def to_list_dict(self):
        """Метод перевода вакансий в список словарей"""
        list_vacancy = []
        for item in self.__all_vacancies:
            list_vacancy.append(item.to_dict())
        return list_vacancy

    def vacancy_from_list(self, vacancy_list):
        """Метод заполнения списка вакансий из файла"""
        self.__all_vacancies = []
        for item in vacancy_list:
            name = item['name']
            url = item['url']
            salary_from = item['salary_from']
            requirement = item['description']
            vacancy = Vacancy(
                name=name,
                url=url,
                salary_from=salary_from,
                requirement=requirement,
            )
            self.__all_vacancies.append(vacancy)

    def print_vacancy(self, number=2):
        '''Метод выведения вакансий'''
        count_list = len(self.__all_vacancies)
        if number > count_list:
            number = count_list
        for index in range(number):
            print(self.__all_vacancies[index])
