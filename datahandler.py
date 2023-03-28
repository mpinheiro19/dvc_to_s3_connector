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

            return values

