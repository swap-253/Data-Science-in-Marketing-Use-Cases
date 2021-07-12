## Problem Statement
In this Problem, the airline company wants cross sell ancilliary/additional products to existing customers to make more money, which means they want to try and get existing customers to get insurance.

The flow of this Analysis will be:
- Creation of a model on the basis of characteristics of customers to determine which customers can be cross sold and in our model we calculate several perfromance metrics like **Accuracy,Precision,Recall,F1 Score,AUC Score and ROC-AUC plots**.

- Use that model to predict the probability that we will successfully cross sell any given customer that we reach out to. 

-  Utilize the above probabilities to calculate the expected profit/loss we are going to incur on every customer we try to cross sell

- In the Last step, we will calculate the maximum expected total profit and the total percent of top propensity customers selling whom we attain it.


## Part 1:- Creation of a Prediction Model
Modelling has been done as follows:-
- The 'ROUTE' column was splitted into two columns which are 'START' and 'END', actually the starting airport and the ending airport.
- Since they had a large number of unique observations, **it didn't make much sense to either Label Encode them or One Hot Encode them**. Hence I used **Target Encoding** on the basis of the
dependent variable(INS_FLAG). The dependent variables has values as 0 or 1. So target encoding just took the means for each of the unique outcomes in these variables. 
- Target Encoding was done for 'geoNetwork_country' column too.
- The 'flight hours' column had values which could be binned for effective prediction, hence I binned that column.
- One Hot Encoding was done for **'PAXCOUNT','SALESCHANNEL','flight_day','flight_hour_cat'** columns. One Hot Encoding was done because these columns didn't contain any heirarchy and 
neither there was issues regarding sparsity.
- 'TRIPTYPEDESC' was Label Encoded.
- Numerical columns which are **'PURCHASELEAD','LENGTHOFSTAY','flightDuration_hour'**were standarised.
- Due to the class imbalance, I used **SMOTE + Tomek** for oversampling and cleaning using Tomek Links.
- Models were built using **Random Forest and xgboost** algorithms and to improve the model parameters, **hyperparameter tuning** was done using **Random Search**
- The model parameters measured were **Accuracy,Precision,Recall,F1 Score and AUC Score** along with **ROC-AUC plots**

## Part 2:- Using our model and expected value to decide which customers to try and sell ancilliary products
I have calculated the probability of every person in the test dataset to be taking the health insurance using our Random Forest Model.
**Consider that the profit attained when the customer buys the airline insurance is Rs 10000 and the cost of selling ancilliary products/insurance is Rs 3500**

![image](https://user-images.githubusercontent.com/75975560/124267212-972ddb00-db55-11eb-91d4-96a7a332fb74.png)

**The above plot implies that the airline gets the maximum profits when it sells insurances to the top 1929 or 19.29% of customers and this value is Rs 4,264,254.38**
 
**For a better understanding open the ipynb notebook** 
