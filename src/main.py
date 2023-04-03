from data_loader import data_loader
import pandas as pd
import datahandler
import yaml, csv


config_file_path = "./data_config.yml"

path_to_file = yaml.safe_load(open(config_file_path))


if __name__== "__main__":   

    df = data_loader(config_file_path)
    dh = datahandler.DataHandler(df)


    # new_values = dh.get_new_entries_from_yml(config_file_path)
    
    # print("New values received from YAML file!\nColumns:")

    # print(*list(
    #     new_values.keys()
    #     ),
    #     sep='\n'
    # )

    # df_columns = list(new_values.keys())

    # print(new_values)

    # with open(path_to_file['data_load']['raw_path'], 'a') as csv_file:
    #     print("Dumping new entries...")
    #     dict_obj = csv.DictWriter(csv_file, df_columns)

    #     dict_obj.writerow(new_values)
    #     print("New row was inserted!")

    dh.normalize_column_names(df)
    print(df.head(1))