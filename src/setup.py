
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd

## Setup topic modelling using LDA in scikit learn

if __name__ == '__main__':

    
    df = pd.read_csv('./data/processed/airline_occurences.csv', sep=';', index_col=0)
    print(df.columns)
    text_col = df["report"]

    n_features = 4
    cv = CountVectorizer(max_df=0.85, min_df= 2, stop_words='english')
    dtm = cv.fit_transform(text_col)

    lda = LatentDirichletAllocation(n_components=n_features, random_state=42)
    topic_results = lda.fit_transform(dtm)

    df['topic'] = topic_results.argmax(axis=1)
    df['cls_topic'] = cv.get_feature_names_out()[df['topic']] # trying to get major topic class needs refinement

    df.to_csv("./data/processed/airline_occurences.csv", sep = ';', index=False)