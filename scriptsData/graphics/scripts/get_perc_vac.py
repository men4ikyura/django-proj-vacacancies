import matplotlib.pyplot as plt
import pandas as pd


def get_plot_perc_years(ax, df):
    area_name = (df["area_name"])
    perc = (df["perc"])

    ax.pie(perc, labels=area_name,  autopct='%1.1f%%',
           textprops={'fontsize': 8}, radius=1.2)


def read_file(path_file):
    return pd.read_csv(path_file)


def create_plot_perc(path_plot, path_file, title):
    fig, ax = plt.subplots()
    fig.suptitle(title)
    df = read_file(path_file)
    get_plot_perc_years(ax, df)
    plt.tight_layout()
    save_plot(fig, path_plot)


def save_plot(fig, path_plot):
    fig.savefig(path_plot,
                dpi=plt.gcf().dpi)


if __name__ == "__main__":
    create_plot_perc("scriptsData/graphics/images/general/perc_vac_plot.png",
                     "scriptsData/generalStatistics/percVacCities.csv", "Доля вакансий по городам")
