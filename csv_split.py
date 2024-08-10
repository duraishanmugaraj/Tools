import pandas as pd
import os 

def split_csv(file_path, num_files):
    base_name = os.path.splitext(os.path.basename("data/creditcard.csv"))[0]
    os.mkdir(base_name)
    # Read the original CSV file
    df = pd.read_csv(file_path)
    
    # Calculate the number of rows per file
    num_rows = len(df)
    rows_per_file = num_rows // num_files
    remainder = num_rows % num_files
    
    # Split the DataFrame and write to new CSV files
    start_row = 0
    for i in range(num_files):
        end_row = start_row + rows_per_file + (1 if i < remainder else 0)
        chunk = df.iloc[start_row:end_row]
        chunk.to_csv(f'{base_name}/{base_name}_part_{i + 1}.csv', index=False)
        start_row = end_row

# Example usage
split_csv('data/creditcard.csv', 4)