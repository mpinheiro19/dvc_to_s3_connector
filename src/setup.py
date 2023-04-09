#nltk.download('popular')
#load_param = "en_core_web_sm"
import spacy
import pandas as pd

## Setup topic modelling using LDA in scikit learn

if __name__ == '__main__':

    
    df = pd.read_csv('./data/processed/airline_occurences.csv', sep=';')

    text_col = df["report"]