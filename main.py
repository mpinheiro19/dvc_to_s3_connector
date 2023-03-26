import csv
import pandas as pd

path_to_file = "data/airline_occurences.csv"

df = pd.read_csv(
    path_to_file
)

if __name__== "__main__":   

    new_values = ['test_report', 'test_pf', 'test_onc', 'test_opp']
    df_columns = df.columns.to_list()

    payload_to_append = dict(zip(df_columns, new_values))

    print(payload_to_append)

    with open(path_to_file, 'a') as csv_file:

        dict_obj = csv.DictWriter(csv_file, df_columns)

        dict_obj.writerow(payload_to_append)