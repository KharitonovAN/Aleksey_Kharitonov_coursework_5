from utils import create_table, add_to_table
from manager import DBManager


def main():
    employers_list = [1740, 15478, 8620, 3529, 78638, 4006]
    dbmanager = DBManager()
    create_table()
    add_to_table(employers_list)

    while True:
        task = input(
            "1. Cписок всех компаний и количество вакансий у каждой компании\n"
            "2. Cписок всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию\n"
            "3. Средняя зарплату по вакансиям\n"
            "4. Список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "5. Список вакансий по ключевому слову\n"
            "0. Завершить работы\n"
        )

        if task == '0':
            break
        elif task == '1':
            print(dbmanager.get_companies_and_vacancies_count())
            print()
        elif task == '2':
            print(dbmanager.get_all_vacancies())
            print()
        elif task == '3':
            print(dbmanager.get_avg_salary())
            print()
        elif task == '4':
            print(dbmanager.get_vacancies_with_higher_salary())
            print()
        elif task == '5':
            keyword = input('Введите ключевое слово: ')
            print(dbmanager.get_vacancies_with_keyword(keyword))
            print()
        else:
            print('Неверный запрос')


main()
