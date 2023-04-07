#nltk.download('popular')
#load_param = "en_core_web_sm"
import spacy
import pandas as pd



if __name__ == '__main__':

    nlp = spacy.load('en_core_web_sm')
    df = pd.read_csv('./data/processed/airline_occurences.csv', sep=';')

    text_col = df["report"]

    for doc in nlp.pipe(df['report'], batch_size=100):
        
        nlp(doc)