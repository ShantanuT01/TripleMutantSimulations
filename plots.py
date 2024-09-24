import matplotlib.pyplot as plt
import pandas as pd

components = ["MP","FC","FS","FM","F2","F3"]
def plot_data(df, title, filename, start, end):
    df = df[df["rmit_factor"].between(start, end)]
    for component in components:
        plt.plot(df["rmit_factor"],df[component]/df[component].max(),label=component)
    plt.xlabel("$R_{mit}$ Percentage Scale Factor")
    plt.ylabel("Component Concentration Normalized")
    plt.title(title)
    plt.gca().invert_xaxis()
    plt.legend()
    plt.savefig(filename, dpi=300)
    plt.clf()

if __name__ == "__main__":
    state = "y"
    aerobic_df = pd.read_csv(f"aerobic_{state}_rmit.csv")
    hypoxic_df = pd.read_csv(f"hypoxic_{state}_rmit.csv")
    aerobic_df = aerobic_df[aerobic_df["rmit_factor"].between(5, 100)]
    hypoxic_df = hypoxic_df[hypoxic_df["rmit_factor"].between(5, 100)]
    fig, axs = plt.subplots(2, 1, sharex=True, sharey=True, tight_layout=True)
    
    for component in components:
        axs[0].plot(aerobic_df["rmit_factor"],aerobic_df[component]/aerobic_df[component].max(),label=component)
    
    for component in components:
        axs[1].plot(hypoxic_df["rmit_factor"],hypoxic_df[component]/hypoxic_df[component].max(),label=component)
    plt.gca().invert_xaxis()
    plt.legend()
    fig.supxlabel('$R_{mit}$ Percent Scale Factor')
    fig.supylabel('Component Concentration Normalized')
    #fig.legend(lines, labels, loc = (0.5, 0), ncol=5)
    fig.set_size_inches(6, 8, forward=True)
    plt.savefig("figures/aerobic_vs_hypoxic_plot.tiff",dpi=300)
    plt.show()