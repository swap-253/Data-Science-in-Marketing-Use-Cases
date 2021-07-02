## 1. Domain Introduction: 
### Customer Segmentation:
Customer segmentation is the practice of dividing a customer base into groups of individuals that are similar in specific ways relevant to marketing, such as age, gender, interests and spending habits.

Customer segmentation relies on identifying key differentiators that divide customers into groups that can be targeted. Information such as a customer's: 

- Demographics (age, race, religion, gender, family size, ethnicity, income, education level)
- Geography (where they live and work)
- Psychographic (social class, lifestyle and personality characteristics) 
- Behavioral (spending, consumption, usage and desired benefits) tendencies 
are taken into account when determining customer segmentation practices.

In this Data Tale we will focus on behavioral Tendencies in order to group Customers into following two categories:
- Loyal Customers
- High Spending Customers


#### Cohort:
A cohort is a group of users sharing a particular characteristic. Strictly speaking it can be any characteristic, but typically the term cohort refers to a time-dependent grouping. For example, a typical cohort groups users by the week or month when they were first acquired. When speaking of groupings that are not time-dependent, the term segment is typically used instead of cohort.

#### Cohort Analysis:
Cohort analysis refers to tracking and investigating the performance of cohorts over time.

For example, if you wanted to see if users you’re acquiring now are more or less valuable than users you’ve acquired in the past, you can define cohorts by the month when they were first acquired. You can then run a cohort analysis to compare year-over-year revenue performance. You can also use cohort Analysis to group users/Customers.

## 2. Problem Statement
In this Data Tale, we will perform Time Cohort Analysis.
Time based Cohort analysis groups the customer by the time they completed their first activity.

The flow of this Analysis will be:
- Segment customers into cohorts based on the month they made their first purchase in.
-  We will then assign a cohort index to each purchase of all the customer. i.e we will mark each transaction based on that customers relative time period difference since his first purchase(Cohort he belongs to).
- Cohort Index assigned  will represent months since the 1st transaction of that particular customer.

- In the Last step, we will calculate various business metrics such as retention rate or Revenue Generated with respect to each Cohort or Quantity Purchased with respect to each Cohort and build a Cohort Chart using Heatmap to represent the results.

## 3. Data Desription:
#### About the dataset.
We will use a randomly subsampled subset of the very popular transactional dataset provided by UCI machine Learning Laboratory.


**Data Set Information:**

This is a transactional data set which contains the transactions occurring between 01/12/2010 and 09/12/2011 for the UK-based a ndregistered non-store online retail firm and contains realistic customer Transaction information in a commonly used format in Industry.


#### Information related to attributes of Dataset is:

- **InvoiceNo**: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. 
- **StockCode**: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product. 
- **Description**: Product (item) name. Nominal. 
- **Quantity**: The quantities of each product (item) per transaction. Numeric.
- **InvoiceDate**: Invice Date and time. Numeric, the day and time when each transaction was generated. 
- **UnitPrice**: Unit price. Numeric, Product price per unit in sterling. 
- **CustomerID**: Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer. 
- **Country**: Country name. Nominal, the name of the country where each customer resides.

The dataset contains 7 columns for each customer transaction representing variuos features of a transaction.

For time cohort analysis, we will use:
- DateTime column
- Price Column
- CustomerID column.

## 6. Cohort Analysis: Retention Rate
Since, We will be performing Cohort Analysis based on Transaction records of Customers, we will be Dealing with Mainly:
- Invoice Data
- CustomerID
- Price 
- and Quantity columns in this Analsyis.

The Following steps will performed to generate the Cohort Chart of Retention Rate :
- **Month Extraction from InvioceDate column**
- **Assigning Cohort to Each Transaction**
- **Assigning Cohort Index to each transaction**
- **Calculating number of unique customers in each Group of (ChortDate,Index)**
- **Creating Cohort Table for Retention Rate**
- **Creating the Cohort Chart using the Cohort Table**

The Detailed information about each step is given below:
## Conclusion:
For e-commerce organisations, cohort analysis is a unique opportunity to find out which clients are the most valuable to their business.

by performing Cohort analysis you can get following answers to following questions:

- How much effective was a marketing campaign held in a particular time period.
- Did the strategy employed to improve the conversion rates of Customers worked?
- Should I focus more on retention rather than acquiring new customers?
- Are my customer nurturing strategies effective?
- Is there a seasonality pattern in Customer behahiour?

#### In this Cohort Analysis we have learnt about:
- Customer Segmentation and it's importance
- Different attributes used for Customer Segmentation 
- Cohort Analysis and It's Advantages
- Application of Cohort Analysis
- Creating Cohort Charts for different business metrics and Analysing them in order to generate insights     

** For more elaborate understanding, open the ipynb notebook.
#
