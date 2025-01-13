from get_count_years import create_plot_count
from get_perc_vac import create_plot_perc
from get_skills_plot import create_plot_skills
from get_sal_cities import create_plot_sal_cities
from get_sal_years import create_plot_sal_years

if __name__ == "__main__":
    create_plot_sal_years(
        "scriptsData/graphics/images/filtred/avg_sal_years.png", "scriptsData/filtredStatistics/filtredAvgSalYears.csv",  "Средняя зарплата по годам для сисадмина")
    create_plot_sal_cities(
        "scriptsData/graphics/images/filtred/avg_sal_cities.png", "scriptsData/filtredStatistics/filtredAvgSalCities.csv", "Средняя зарплата по городам для сисадмина")
    create_plot_skills(
        "scriptsData/graphics/images/filtred/skills_plots", "scriptsData/filtredStatistics/filtredSkills.json")
    create_plot_perc(
        "scriptsData/graphics/images/filtred/perc_vac_plot.png", "scriptsData/filtredStatistics/percCities.csv", "Доля вакансий по городам для сисадмина")
    create_plot_count(
        "scriptsData/graphics/images/filtred/count_vac_years.png", "scriptsData/filtredStatistics/filtredCountYears.csv", "Количество вакансий по годам для сисадмина")
