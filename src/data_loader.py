import yaml,csv
import pandas as pd

def data_loader(config_path : str) -> pd.DataFrame:
    
    """
    Data Loader function created for better versioning and experiment tracking
    
    Args:
        config_path (configuration yaml file) : string.

    """
    try:

        _file_extension_assertion(config_path)

    except AssertionError:

        raise AssertionError("Configuration file must be yml file!")  
    
    else:

        configuration_file = yaml.safe_load(open(config_path))
        data_path = configuration_file['data_load']['raw_path']
    
    # needs assertion for csv files as well
    
    return pd.read_csv(data_path)

def _file_extension_assertion(config_path : str):

    assert config_path.endswith(".yml")

def insert_csvrow_from_yaml(new_values, path_to_file) -> None:

    print(*list(
        new_values.keys()
        ),
        sep='\n'
    )

    df_columns = list(new_values.keys())

    print(new_values)

    with open(path_to_file['data_load']['raw_path'], 'a') as csv_file:
        print("Dumping new entries...")
        dict_obj = csv.DictWriter(csv_file, df_columns)

        dict_obj.writerow(new_values)
        print("New row was inserted!")
