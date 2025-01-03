import matplotlib.pyplot as plt
import pandas as pd


def get_plot_sal_cities(ax):
    df = pd.read_csv("scriptsData/generalStatistics/avg_salary_cities.csv")
    people = (df["area_name"])
    salary = (df["average"] / 1000)

    ax[0, 0].set_title('Средняя з/п по городам', fontsize=8)
    ax[0, 0].barh(people, salary)
    ax[0, 0].tick_params(axis='y', labelsize=4)
    ax[0, 0].set_xticks([50 + 5 * i for i in range(11)])
    ax[0, 0].invert_yaxis()
    ax[0, 0].set_xlabel("cредняя з/п (тыс. руб)", fontsize=6)
    ax[0, 0].tick_params(axis='x', labelsize=4, rotation=90)
    ax[0, 0].grid(axis='x')


def get_plot_sal_years(ax):
    df = pd.read_csv("scriptsData/generalStatistics/avg_salary_years.csv")
    years = (df["published_at"])
    salary = (df["average"] / 1000)

    ax[0, 1].set_title('Средняя з/п по годам', fontsize=8)
    ax[0, 1].bar(years, salary, width=0.7)
    ax[0, 1].set_ylabel("cредняя з/п (тыс. руб)", fontsize=6)
    ax[0, 1].tick_params(axis='y', labelsize=4)
    ax[0, 1].set_xticks(years, labels=years)
    ax[0, 1].tick_params(axis='x', labelsize=4, rotation=90)
    ax[0, 1].grid(axis='y')


def get_plot_count_years(ax):
    df = pd.read_csv("scriptsData/generalStatistics/countYears.csv")
    years = (df["published_at"])
    size = (df["size"] / 1000)

    ax[1, 0].set_title('Количество вакансий по годам', fontsize=8)
    ax[1, 0].bar(years, size, width=0.7)
    ax[1, 0].set_ylabel("количесвто (тыс.)", fontsize=6)
    ax[1, 0].tick_params(axis='y', labelsize=4)
    ax[1, 0].set_xticks(years, labels=years)
    ax[1, 0].tick_params(axis='x', labelsize=4, rotation=90)
    ax[1, 0].grid(axis='y')


def get_plot_perc_years(ax):
    df = pd.read_csv("scriptsData/generalStatistics/percVacCities.csv")
    area_name = (df["area_name"])
    perc = (df["perc"])

    ax[1, 1].set_title('Доля вакансий по городам', fontsize=8)
    ax[1, 1].pie(perc, labels=area_name,  autopct='%1.1f%%',
                 textprops={'fontsize': 4}, radius=1.2)


if __name__ == "__main__":
    fig, ax = plt.subplots(2, 2)

    fig.suptitle("Общая аналитика по профессиям")
    get_plot_sal_cities(ax)
    get_plot_sal_years(ax)
    get_plot_count_years(ax)
    get_plot_perc_years(ax)
    plt.tight_layout()

    fig.savefig("scriptsData/graphics/images/generalGraphics.png",
                dpi=plt.gcf().dpi)
    plt.close()
