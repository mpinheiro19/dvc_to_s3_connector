from data_loader import data_loader
import pandas as pd
import datahandler
import yaml, nltk


config_file_path = "./data_config.yml"
path_to_file = yaml.safe_load(open(config_file_path))



if __name__== "__main__":

    #nltk.download('popular')  

    df = data_loader(config_file_path)
    dh = datahandler.DataHandler(df)
    #new_values = dh.get_new_entries_from_yml(config_file_path)

    dh.normalize_column_names(df)
    dh.strip_blank_spaces(df)
    
    df["is_precautionary_procedures"] = dh.check_column_condition(
        col = df.occurence_precautionary_procedures,
        condition = ["NONE", "OTHER"]           #should move this object to yaml file for better experimentation
        )
    
    df["is_major_failure"] = dh.check_string_expression(
        df['part_failure'].str.lower(),
        expression=['failed','damaged', 'collapsed']    #should move this object to yaml file for better experimentation
    )

    df.to_csv(
        'data/processed/airline_occurences.csv',
        sep=';'
    )