import matplotlib.pyplot as plt

def show_total_production(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['total_production'], marker='o')
    plt.title('Total Production Over Time')
    plt.xlabel('Time Step')
    plt.ylabel('Total Production')
    plt.grid(True)
    plt.tight_layout()
    return plt
