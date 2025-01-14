import matplotlib.pyplot as plt
import pandas as pd


def get_plot_sal_cities(ax, df):
    people = (df["area_name"])
    salary = (df["average"] / 1000)

    ax.barh(people, salary)
    ax.tick_params(axis='y', labelsize=9)
    ax.invert_yaxis()
    ax.set_xlabel("cредняя з/п (тыс. руб)", fontsize=11)
    ax.tick_params(axis='x', labelsize=9, rotation=90)
    ax.grid(axis='x')


def read_file(path_file):
    return pd.read_csv(path_file)


def create_plot_sal_cities(path_plot, path_file, title):
    fig, ax = plt.subplots()
    fig.suptitle(title)
    df = read_file(path_file)
    get_plot_sal_cities(ax, df)
    plt.tight_layout()
    save_plot(fig, path_plot)


def save_plot(fig, path_plot):
    fig.savefig(path_plot,
                dpi=plt.gcf().dpi)


if __name__ == "__main__":
    create_plot_sal_cities("scriptsData/graphics/images/general/avg_sal_cities.png",
                           "scriptsData/generalStatistics/avg_salary_cities.csv", "Средняя зарплата по городам")
