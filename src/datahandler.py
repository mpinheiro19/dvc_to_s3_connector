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

    def strip_blank_spaces(self, df : pd.DataFrame) -> None:
        """
        remove blank spaces in object pandas.Series

        Args:
            df (pandas.DataFrame) : dataframe to be treated
        """

        string_columns = df.select_dtypes('object').columns.to_list()

        for col in string_columns:

            print(f"removing blank spaces in string {col} column .....")
            df[col] = df[col].str.strip()
        
        print("Done!")

    def check_column_condition(self, col : pd.Series, condition : list) -> pd.Series:
        """
        Generate boolean series based on existence of certain element list condition.
        Returns a boolean column.

        Args:
            col (pandas.Series) : pd.Series to be evaluated
            condition (list) : list of values to check 
        """

        return col.isin(condition)
    
    def check_string_expression(self, col : pd.Series, expression : list) -> pd.Series:
        """
        Generate boolean series based on existence of certain expressions/words list.
        Returns a boolean column.

        Args:
            col (pandas.Series) : pd.Series to be evaluated
            condition (list) : list of expressions to query    
        """

        raise NotImplementedError("TBD")

