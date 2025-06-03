#v1
import csv

# Function to load the data from the "data" csv to the "data" dictionary
def load_data_to_dict(filename):
    data = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i, row_dict in enumerate(reader):
            data[i] = dict(row_dict)  # Convert each row into a dictionary and store it with key i to a bigger dictionary named "data"
    return data


if __name__ == "__main__":
    filename = "data.csv"
   
   #Get the data from the CSV into the form of a dictionary
    dataset_dict = load_data_to_dict(filename)
    
    
    for i in range(20):
        print(f"Row / Patient {i}:", dataset_dict[i])
