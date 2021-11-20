import os
import numpy as np
from joblib import load
from lime.lime_text import LimeTextExplainer
from sklearn.pipeline import make_pipeline

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

class ModelApplicationRepository():

    def model_application(self, df):
        count_vectorizer = load(os.path.join(THIS_FOLDER, 'model_application/bow.save'))
        model = load(os.path.join(THIS_FOLDER, 'model_application/model.save'))
        
        X = count_vectorizer.transform(df['tweet_content'])
        result = model.predict(X)
        
        total = result.size
        positives = np.count_nonzero(result == 1)
        negatives = total - positives

        c = make_pipeline(count_vectorizer, model)
        tweets_list = list(df['tweet_content'])
        class_names = {0.0: 'negative', 1.0:'positive'}
        explainer = LimeTextExplainer(class_names=class_names)

        words = []
        for tweet in tweets_list:
            if tweet is not np.nan:
                exp = explainer.explain_instance(tweet, c.predict_proba)
                words.append(exp.as_list()[0])
        
        positives_explained = []
        negatives_explained = []

        for word in words:
            if word[1] < 0:
                negatives_dict = {
                    'word': word[0],
                    'relevance': round(word[1], 4)
                }
                negatives_explained.append(negatives_dict)
            elif word[1] > 0:
                positives_dict = {
                    'word': word[0],
                    'relevance': round(word[1], 4)
                }
                positives_explained.append(positives_dict)

        return positives, negatives, positives_explained, negatives_explained