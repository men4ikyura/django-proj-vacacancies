import json
import matplotlib.pyplot as plt
import os


def read_file(path_file):
    with open(path_file) as file:
        return json.load(file)


def get_plot_skills(data, path_plot):
    for year in data.keys():
        fig, ax = plt.subplots()
        fig.suptitle(f"ТОП-20 навыков за {year} год")
        skills = []
        counts = []
        for item in data[year]:
            skills.append(item[0])
            counts.append(item[1])
        ax.barh(skills, counts)
        ax.tick_params(axis='y', labelsize=6)
        ax.tick_params(axis='x', labelsize=6)
        ax.set_xlabel("Количество умопинаний за год", fontsize=8)
        ax.grid(axis='x')
        plt.tight_layout()
        cur_path_plot = os.path.join(path_plot, f"{year}_skill_plot.png")
        save_plot(fig, cur_path_plot)
        plt.close()


def create_plot_skills(path_plot, path_file):
    df = read_file(path_file)
    get_plot_skills(df, path_plot)


def save_plot(fig, path_plot):
    fig.savefig(path_plot,
                dpi=plt.gcf().dpi)


if __name__ == "__main__":
    create_plot_skills("scriptsData/graphics/images/general/skills_plots",
                       "scriptsData/generalStatistics/trend_skills.json")
