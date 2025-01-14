import matplotlib.pyplot as plt
import pandas as pd


def get_plot_count_years(ax, df):
    years = (df["published_at"])
    size = (df["size"] / 1000)
    ax.bar(years, size, width=0.7)
    ax.set_ylabel("количесвто (тыс.)", fontsize=11)
    ax.tick_params(axis='y', labelsize=9)
    ax.set_xticks(years, labels=years)
    ax.tick_params(axis='x', labelsize=9, rotation=90)
    ax.grid(axis='y')


def read_file(path_file):
    return pd.read_csv(path_file)


def create_plot_count(path_plot, path_file, title):
    fig, ax = plt.subplots()
    fig.suptitle(title)
    df = read_file(path_file)
    get_plot_count_years(ax, df)
    plt.tight_layout()
    save_plot(fig, path_plot)


def save_plot(fig, path_plot):
    fig.savefig(path_plot,
                dpi=plt.gcf().dpi)


if __name__ == "__main__":
    create_plot_count("scriptsData/graphics/images/general/count_vac_years.png",
                      "scriptsData/generalStatistics/countYears.csv", "Количество вакансий по годам")
