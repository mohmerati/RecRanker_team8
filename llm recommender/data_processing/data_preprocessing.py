import pandas as pd

def calculate_user_importance(file_path):
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Ensure the dataset has the required columns
    if 'user_id' not in df.columns:
        raise ValueError("Dataset must contain 'user_id' column")
    
    # Calculate the number of interactions for each user
    user_interactions = df['user_id'].value_counts().reset_index()
    user_interactions.columns = ['user_id', 'interaction_count']
    
    return user_interactions

# Example usage
if __name__ == "__main__":
    file_path = 'path_to_your_dataset.csv'
    user_importance = calculate_user_importance(file_path)
    print(user_importance)
    # Calculate the total number of interactions
    total_interactions = user_interactions['interaction_count'].sum()
    
    # Calculate the probability for each user
    user_interactions['interaction_probability'] = user_interactions['interaction_count'] / total_interactions
    
    return user_interactions