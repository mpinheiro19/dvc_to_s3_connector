import csv
import pandas as pd
import datahandler as feats

path_to_file = "data/raw/airline_occurences.csv"

df = pd.read_csv(
    path_to_file
)

dh = feats.DataHandler(df)


if __name__== "__main__":   

    new_values = dh.get_new_entries_from_yml('./data_config.yml')
    
    print("New values received from YAML file!\nColumns:")
    print(*list(
        new_values.keys()
        ),
        sep='\n'
    )

    df_columns = list(new_values.keys())

    with open(path_to_file, 'a') as csv_file:
        print("Dumping new entries...")
        dict_obj = csv.DictWriter(csv_file, df_columns)

        dict_obj.writerow(new_values)
        print("New row was inserted!")