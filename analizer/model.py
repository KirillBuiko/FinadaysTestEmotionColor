import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_score, recall_score
from tokenizer import tokenize_sentence
import joblib


class SentenceEmotionColorModel:
    def __init__(self, language: str, dataset: pd.DataFrame) -> None:
        self.__df = dataset
        def tokenazer(x): return tokenize_sentence(x, language=language)
        self.__model_pipelene = Pipeline([
            ("vectorizer", TfidfVectorizer(tokenizer=tokenazer)),
            ('model', LogisticRegression(random_state=0))
        ])

    def fit(self):
        self.__model_pipelene.fit(self.__df['comment'], self.__df['type'])

    def test(self):
        return {
            'precision':
            precision_score(
                y_true=self.__df["type"],
                y_pred=self.__model_pipeline_ru.predict(self.__df["comment"])),
            'recall':
            recall_score(
                y_true=self.__df["type"],
                y_pred=self.__model_pipeline_ru.predict(self.__df["comment"])
            )}

    def predict(self, sentence: str):
        return self.__model_pipelene.predict([sentence])

    def predict_proba(self, sentence: str):
        return self.__model_pipelene.predict_proba([sentence])

    def save(self, filename: str):
        joblib.dump(self.__model_pipelene, filename)


if __name__ == '__main__':
    df = pd.read_csv("./data/dataset_train_english.csv", sep=",")
    df['type'] = df['type'].apply(int)
    model = SentenceEmotionColorModel('english', df)
