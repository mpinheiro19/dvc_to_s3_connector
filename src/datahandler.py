import yaml
import pandas as pd

class DataHandler():
    """
    Data Handler Object for Feature Engineering purpose
    """

    def __init__(self, df : pd.DataFrame) -> None:
        """
        __init__ method.  
        
        Args:
            df (pd.DataFrame): pd.DataFrame.
        """
        self.df = df
        print("Data Handler Object instance created successfully!")
    
    def get_new_entries_from_yml(self, path_to_yml : object) -> dict:

        """
        obtain new inputs for dataframe from yml file
        
        Args:
            path_to_yml (object) : object
        """

        with open(path_to_yml,"r") as f:
            
            values = yaml.safe_load(f)

            return values['data_append']
        
    def get_path_to_csv_file(self, path_to_yml : object) -> object:

        """
        Extract path to csv file
        
        Args:
            path_to_yml (object) : object
        """

        with open(path_to_yml,"r") as f:
            
            values = yaml.safe_load(f)

            return values['data_load']['raw_path']
        
    def normalize_column_names(self, df : pd.DataFrame) -> None:

        """
        normalize column names removing spaces and lowercasing each

        Args:
            df (pandas.DataFrame) : pandas dataframe to change column names
        """

        new_column_names = [
            str(
                col.replace(" " , "_")      # remove blank spaces
            ).lower()                       # lowercase string column
            for col 
            in df.columns
        ]

        df.columns = new_column_names
