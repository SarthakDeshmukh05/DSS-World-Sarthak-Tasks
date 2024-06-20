import pandas as pd

# Define the height threshold for infants
INFANT_HEIGHT_THRESHOLD = 1.2  # Adjust as necessary based on your criteria

# Load the dataset
def load_dataset(filepath):
    return pd.read_csv(filepath)

# Function to classify and count infants and adults
def classify_individuals(data):
    infants = 0
    adults = 0

    for _, row in data.iterrows():
        if row['Height'] < INFANT_HEIGHT_THRESHOLD:
            infants += 1
        else:
            adults += 1

    return infants, adults

# Main function
def main():
    # Load the dataset (replace 'data.csv' with the actual file path)
    dataset_path = '/content/Book1.csv'
    data = load_dataset(dataset_path)

    # Classify and count infants and adults
    infants, adults = classify_individuals(data)

    # Output the results
    print(f"Number of infants: {infants}")
    print(f"Number of adults: {adults}")

if __name__ == "__main__":
    main()
