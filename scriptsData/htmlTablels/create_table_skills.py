from prettytable import PrettyTable
import json
import os


def read_file(path_file):
    with open(path_file) as file:
        return json.load(file)


def create_html_string(data, html_file_dir):
    for year in data.keys():
        table = PrettyTable(["Название навыка", "Количество упоминаний"])
        for skill in data[year]:
            table.add_row([skill[0], str(skill[1])])
        save_html_string_in_file(os.path.join(
            html_file_dir, f"{year}skills.html"), table.get_html_string())


def save_html_string_in_file(path_file, html_string):
    with open(path_file, 'w') as file:
        file.write(html_string)


def create_html_file(data_file_name, html_file_dir):
    data = read_file(data_file_name)
    create_html_string(data, html_file_dir)


if __name__ == "__main__":
    create_html_file("scriptsData/generalStatistics/trend_skills.json",
                     "scriptsData/htmlTablels/htmlFiles/general/skills")
    create_html_file("scriptsData/filtredStatistics/filtredSkills.json",
                     "scriptsData/htmlTablels/htmlFiles/filtred/skills")
