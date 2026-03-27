based on : Bayes' Theorem (https://www.youtube.com/watch?v=JsfOXk7qmSM)

calculate 
spam | words in email 


core formula used : 
p(spam|word) = P(word|spam).p(spam)/p(word)

p(spam|word) : the probability that the email is spam given the word is present. 

p(word|spam) : the probability that the word appears is knonw spam emails (calculated from your training data). 

p(spam) the overall probability of any email being spam (e.g. if 20 out of 100 total emails are spam P(Spam)=0.2)

p(word) the overall probability of the word appearing in any email (spam or ham)
 

The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification). The multinomial distribution normally requires integer feature counts. However, in practice, fractional counts such as tf-idf may also work.

from sklearn.naive_bayes import MultinomialNB
