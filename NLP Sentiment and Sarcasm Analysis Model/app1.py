from flask import Flask,render_template,url_for,request
#import pandas as pd 
import pickle
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout ,BatchNormalization,Reshape,Dot,Concatenate,Add,Lambda,Input,Embedding
from tensorflow.keras.optimizers import Adam,SGD,Adagrad,Adadelta,RMSprop
from tensorflow.keras.models import Model
from tensorflow.keras.regularizers import l2
from keras.layers.recurrent import LSTM
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
# load the model from disk
#filename = 'nlp_model.pkl'
#clf = pickle.load(open(filename, 'rb'))
lstm_model = load_model('lstm_model.h5')
sarcasm_model = load_model('sarcasm_model.h5')
cv1=pickle.load(open('transform.pkl','rb'))
cv=pickle.load(open('transform2.pkl','rb'))
tk=pickle.load(open('tokenizer_obj.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home1.html')

@app.route('/predict',methods=['POST'])
def predict():
#	df= pd.read_csv("spam.csv", encoding="latin-1")
#	df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
#	# Features and Labels
#	df['label'] = df['class'].map({'ham': 0, 'spam': 1})
#	X = df['message']
#	y = df['label']
#	
#	# Extract Feature With CountVectorizer
#	cv = CountVectorizer()
#	X = cv.fit_transform(X) # Fit the Data
#    
#    pickle.dump(cv, open('tranform.pkl', 'wb'))
#    
#    
#	from sklearn.model_selection import train_test_split
#	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#	#Naive Bayes Classifier
#	from sklearn.naive_bayes import MultinomialNB
#
#	clf = MultinomialNB()
#	clf.fit(X_train,y_train)
#	clf.score(X_test,y_test)
#    filename = 'nlp_model.pkl'
#    pickle.dump(clf, open(filename, 'wb'))
    
	#Alternative Usage of Saved Model
	# joblib.dump(clf, 'NB_spam_model.pkl')
	# NB_spam_model = open('NB_spam_model.pkl','rb')
	# clf = joblib.load(NB_spam_model)

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv1.transform(data).toarray()
		my_prediction2 = clf.predict(vect)
		# my_prediction2 = lstm_model.predict_classes(np.array(k))
		vect = tk.texts_to_sequences(data)
		test_review_pad = pad_sequences(vect, maxlen=25, padding='post')
		my_prediction1 = sarcasm_model.predict_classes(test_review_pad)
	return render_template('result1.html',prediction2 = my_prediction2,prediction1=my_prediction1)



if __name__ == '__main__':
	app.run(debug=True)
