from prettytable import PrettyTable


def create_html_string(data, headers):
    table = PrettyTable([*headers])
    for i in range(1, len(data)):
        table.add_row(data[i].split(','))

    return table.get_html_string()


def read_file(file_name):
    with open(file_name) as file:
        return file.readlines()


def save_html_string_in_file(path_file, html_string):
    with open(path_file, 'w') as file:
        file.write(html_string)


def create_html_file(data_file_name, html_file_name, headers):
    data = read_file(data_file_name)
    html_string = create_html_string(data, headers)
    save_html_string_in_file(html_file_name, html_string)


if __name__ == "__main__":
    create_html_file("scriptsData/generalStatistics/avg_salary_cities.csv",
                     "scriptsData/htmlTablels/htmlFiles/general/avgSalaryCities.html", ["Город", "Средняя зарплата (рубли)"])
    create_html_file("scriptsData/generalStatistics/avg_salary_years.csv",
                     "scriptsData/htmlTablels/htmlFiles/general/avgSalaryYears.html", ["Год", "Средняя зарплата (рубли)"])
    create_html_file("scriptsData/generalStatistics/countYears.csv",
                     "scriptsData/htmlTablels/htmlFiles/general/countYears.html", ["Город", "Количество вакансий"])
    create_html_file("scriptsData/generalStatistics/percVacCities.csv",
                     "scriptsData/htmlTablels/htmlFiles/general/percVacCities.html", ["Город", "Доля вакансий"])

    create_html_file("scriptsData/filtredStatistics/filtredAvgSalCities.csv",
                     "scriptsData/htmlTablels/htmlFiles/filtred/filtredAvgSalCities.html", ["Город", "Средняя зарплата (рубли)"])
    create_html_file("scriptsData/filtredStatistics/filtredAvgSalYears.csv",
                     "scriptsData/htmlTablels/htmlFiles/filtred/filtredAvgSalYears.html", ["Год", "Средняя зарплата (рубли)"])
    create_html_file("scriptsData/filtredStatistics/filtredCountYears.csv",
                     "scriptsData/htmlTablels/htmlFiles/filtred/filtredCountYears.html", ["Город", "Количество вакансий"])
    create_html_file("scriptsData/filtredStatistics/percCities.csv",
                     "scriptsData/htmlTablels/htmlFiles/filtred/percVacCities.html", ["Город", "Доля вакансий"])
