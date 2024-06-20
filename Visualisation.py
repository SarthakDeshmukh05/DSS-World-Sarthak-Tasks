import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_dataset(filepath):
    return pd.read_excel('/content/Book1.xlsx')

# Function to process and calculate boardings and deboardings
def calculate_boarding_deboarding(data):
    boarding_counts = {'Stop': [], 'Adults_boarded': [], 'Infants_boarded': [], 'Adults_deboarded': [], 'Infants_deboarded': []}

    boarding_counts['Stop'].append(data.loc[0, 'Stop'])
    boarding_counts['Adults_boarded'].append(data.loc[0, 'Adults_aboard'])
    boarding_counts['Infants_boarded'].append(data.loc[0, 'Infants_aboard'])
    boarding_counts['Adults_deboarded'].append(0)
    boarding_counts['Infants_deboarded'].append(0)

    for i in range(1, len(data)):
        stop = data.loc[i, 'Stop']
        adults_boarded = data.loc[i, 'Adults_aboard'] - data.loc[i-1, 'Adults_aboard']
        infants_boarded = data.loc[i, 'Infants_aboard'] - data.loc[i-1, 'Infants_aboard']
        adults_deboarded = -adults_boarded if adults_boarded < 0 else 0
        infants_deboarded = -infants_boarded if infants_boarded < 0 else 0
        adults_boarded = max(adults_boarded, 0)
        infants_boarded = max(infants_boarded, 0)

        boarding_counts['Stop'].append(stop)
        boarding_counts['Adults_boarded'].append(adults_boarded)
        boarding_counts['Infants_boarded'].append(infants_boarded)
        boarding_counts['Adults_deboarded'].append(adults_deboarded)
        boarding_counts['Infants_deboarded'].append(infants_deboarded)

    return pd.DataFrame(boarding_counts)

# Function to visualize the data
def visualize_boarding_deboarding(data, boarding_deboarding_data):
    sns.set(style="whitegrid")

    fig, ax = plt.subplots(4, 1, figsize=(14, 24), sharex=True)

    # Plot boardings
    sns.barplot(x='Stop', y='Adults_boarded', data=boarding_deboarding_data, ax=ax[0], color='b', label='Adults Boarded')
    sns.barplot(x='Stop', y='Infants_boarded', data=boarding_deboarding_data, ax=ax[0], color='g', label='Infants Boarded')
    ax[0].set_title('Number of People Boarded at Each Stop')
    ax[0].legend()

    # Plot deboardings
    sns.barplot(x='Stop', y='Adults_deboarded', data=boarding_deboarding_data, ax=ax[1], color='b', label='Adults Deboarded')
    sns.barplot(x='Stop', y='Infants_deboarded', data=boarding_deboarding_data, ax=ax[1], color='g', label='Infants Deboarded')
    ax[1].set_title('Number of People Deboarded at Each Stop')
    ax[1].legend()

    # Plot cumulative people on board
    data['Total_onboard'] = data['Adults_aboard'] + data['Infants_aboard']
    sns.lineplot(x='Stop', y='Total_onboard', data=data, ax=ax[2], marker='o', label='Total Onboard')
    sns.lineplot(x='Stop', y='Adults_aboard', data=data, ax=ax[2], marker='o', label='Adults Onboard')
    sns.lineplot(x='Stop', y='Infants_aboard', data=data, marker='o', ax=ax[2], label='Infants Onboard')
    ax[2].set_title('Cumulative Number of People Onboard')
    ax[2].legend()

    plt.xlabel('Stop')
    plt.ylabel('Number of People')
    plt.tight_layout()
    plt.show()

    # Additional scatter plot for weight distribution
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.scatterplot(x='Stop', y='Total_weight', data=data, hue='Stop', palette='viridis', ax=ax)
    ax.set_title('Total Weight at Each Stop')
    plt.xlabel('Stop')
    plt.ylabel('Total Weight (kg)')
    plt.show()

    # Pie charts for the proportion of adults and infants at each stop
    for stop in data['Stop'].unique():
        stop_data = data[data['Stop'] == stop]
        adults = stop_data['Adults_aboard'].values[0]
        infants = stop_data['Infants_aboard'].values[0]
        labels = ['Adults', 'Infants']
        sizes = [adults, infants]
        colors = ['blue', 'green']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        plt.title(f'Proportion of Adults and Infants at Stop {stop}')
        plt.show()

# Main function
def main():
    # Load the dataset (replace 'data.csv' with the actual file path)
    dataset_path = '/content/Book1.xlsx'
    data = load_dataset(dataset_path)

    # Calculate boarding and deboarding
    boarding_deboarding_data = calculate_boarding_deboarding(data)

    # Visualize the data
    visualize_boarding_deboarding(data, boarding_deboarding_data)

if __name__ == "__main__":
    main()
