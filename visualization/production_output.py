import matplotlib.pyplot as plt

def show_total_production(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['total_production'], marker='o')
    ax.set_title('Total Production Over Time')
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Total Production')
    ax.grid(True)
    plt.tight_layout()
    return fig  # returning figure instead of plt directly
