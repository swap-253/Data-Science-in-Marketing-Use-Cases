In this repository I have utilised 6 different NLP Models to predict the sentiments of the user as per the twitter reviews on airline. The dataset is 
Twitter US Airline Sentiment. The best models each from ML and DL have been deployed using **Flask and Heroku platform**. The dataset has been imported from Kaggle with the following link:- 
https://www.kaggle.com/crowdflower/twitter-airline-sentiment/download
<br>
<br>
The text preprocessing involved removal of stopwords,HTML Tags,punctuations and lemmatization taking care of POS Tags.I have used six methodologies for this classification.
### Sentiment Analysis Using Machine And Deep Learning
**1) Without Any Vectorization**
<br>
Here I have just used a dictionary of most frequent 2500 words. So my training set includes a dictionary of top 2500 words after text preprocessing with true 
or false as the values of dictionary whether they occured in the sentence or not. Here I have used all 3 labels positive,negative and neutral and plotted a 
confusion matrix. The accuracy was observed around 78% accuracy with 86-87% of precison and recall.
<br>
**2) Using Machine Learning Algorithms like Naive Bayes, K Nearest Neighbors and Random Forests**
<br>
Here I used vectorization techniques such as Bag of Words, TF-IDF and word2Vec to use textual information and utilised the above machine learning algorithms
along with hyperparameter tuning for sentiment analysis. The Multinomial Naive Bayes Model acheived 89% accuracy and 0.95 AUC score while the KNN and Random Forest 
Models acheived accuracies of around 85-87% and AUC scores of 0.92.
<br>
Here the best results were attained by **Multinomial Naive Bayes**. Hence I created its **pickle file** and deployed on Flask and Heroku. Click the link below and enter the text whose sentiment you wanna know.
<br>
https://firstnlpdeployedapp.herokuapp.com/
<br>
**3) Using Deep Learning**
<br>
**Part A)** Here I used Artificial Neural Networks with only Dense Layers and two Dropout Layers. Initially I displayed the effect of regularization and dropout layer
on our prediction. After that I did hyperparamter tuning using **Keras Tuner** and acheived test and validation set accuracies of around 92-93% 
<br>
**Part B)** Here I used Embedding Layers and LSTMs alongside Dense and Dropout Layers. I further did hyperparameter tuning for each of the Embedding, LSTM and Dense
layers using Keras Tuner and acheived 98% accuracy on test set and around 93% on validation set in just 4 iterations.
<br>
**Part C)** Here I used Embedding Layers and Bidirectional LSTM alongside Dense and Dropout Layers. I further did hyperparameter tuning for each of the Embedding, Bidirectional LSTM and Dense layers using Keras Tuner and acheived 97.23% accuracy on test set and around 94.26% on validation set in just 4 iterations.
<br>
Here the best results were attained by **LSTM Model**. Hence I created its **file as lstm_model.h5** and deployed it on Flask. Its size was above 25 MB leading to difficulty of upload. So its jupyter notebook has been added in the folder **Deep Learning Models with deployment on flask** which downloads lstm_model.h5 in **Google Colab**.
<br>
## Sarcasm Detection
I also created a model for Sarcasm Detection of customer tweets which was trained on the Sarcasm Headlines dataset from kaggle with the link as
**https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection** which contained the labels as whether the article's headline was sarcastic or not.
<br>
 I did the text preprocessing which involved removal of **emojis or unneccesaary symbols, maps and flag symbols**. **Punctuations and stopwords were removed**. Keras text tokenizer was
 used to tokenize the text or for the vectorization of our text.So each word was given an index starting from 1.
 <br>
 Then I used **Stanford NLP's pretrained GloVe embeddings** which basically means that there was an embedding for almost each of the words in our corpus and we are going to use those 
 embeddings to create a model to detect whether a tweet is sarcastic or not. Our model included an embedding layer consisting of GloVe embeddings and this layer couldn't be trained which 
 is obvious. It further included an LSTM Layer and a Dense Layer.
 <br>
 **After 10 iterations, it attained a test set accuracy of around 88%.**
 Now comes the API creation part. So whenever I would enter a tweet, the sentiments as well as the presence of sarcasm will be detected in the message. For example look at the below pictures:-
 <br>
 ## Screenshots
 ### Example 1
#### Before clicking the predict button
![image](https://user-images.githubusercontent.com/75975560/124671285-e1ef8000-ded2-11eb-8338-665d69814e2e.png)
#### After clicking the predict button
![image](https://user-images.githubusercontent.com/75975560/124671464-23802b00-ded3-11eb-8803-8036849c10a2.png)
### Example 2
#### Before clicking the predict button
![image](https://user-images.githubusercontent.com/75975560/124671592-575b5080-ded3-11eb-9274-c75720dd0b97.png)
#### After clicking the predict button
![image](https://user-images.githubusercontent.com/75975560/124671639-680bc680-ded3-11eb-956d-1f2229fddec2.png)
### Example 3
#### Before clicking the predict button
![image](https://user-images.githubusercontent.com/75975560/124671928-d9e41000-ded3-11eb-81a7-5a293b072b84.png)
#### After clicking the predict button
![image](https://user-images.githubusercontent.com/75975560/124671969-e9635900-ded3-11eb-95a3-b422eb3574f9.png)
### Example 4
#### Before clicking the predict button
![image](https://user-images.githubusercontent.com/75975560/124672073-10218f80-ded4-11eb-9c88-29c44fa71f7f.png)
#### After clicking the predict button
![image](https://user-images.githubusercontent.com/75975560/124672103-1c0d5180-ded4-11eb-9d36-e53945dbce75.png)
