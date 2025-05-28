# Start: Data Preprocessing
import re
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

all_stopwords = stopwords.words('english')
all_stopwords.remove('not')

def preprocess_reviews(dataset):
    def clean_review(review):
        review = re.sub('[^a-zA-Z]', ' ', review)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
        review = ' '.join(review)
        return review

    corpus = []
    for i in range(len(dataset['Review'])):
        corpus.append(clean_review(dataset['Review'][i]))
    return corpus


     



     
