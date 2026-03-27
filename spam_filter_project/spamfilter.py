# import libraries
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# create dataset 
data = {
    'text': [
        'Win money now', 
        'Limited offer click now', 
        'Meeting at 5 pm',
        'Project discussion tomorrow', 
        'Free lottery win', 
        'lets have lunch',
        'congratulations you won prize', 
        'call me when free', 
    ], 
    'label': [1, 1, 0, 0, 1, 0, 1, 0]  #1-spam, 0-not spam
}


# convert dataframe
df=pd.DataFrame(data)

# convert test -> numbers 
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y= df['label']

# train model (Naive Bayes)
model = MultinomialNB()
model.fit(X, y)

# Test/Prediction 
test_email = ["Project discussion tomorrow"]

# convert test email 
test_vector = vectorizer.transform(test_email)

# prediction 
prediction = model.predict(test_vector)[0]
probability = model.predict_proba(test_vector)[0]

print("Email : ", test_email[0])
print("Prediction: ", "spam" if prediction==1 else "not spam")

print("spam probability: " , round(probability[1]*100, 2), "%")
print("not spam probability: ", round(probability[0]*100, 2), "%")