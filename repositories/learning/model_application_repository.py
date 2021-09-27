import os
import numpy as np
from joblib import load

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

        return (positives/total)*100, (negatives/total)*100