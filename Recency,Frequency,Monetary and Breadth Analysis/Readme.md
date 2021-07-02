## 1. Domain Introduction: 
### Customer Segmentation:
Customer segmentation is the practice of dividing a customer base into groups of individuals that are similar in specific ways relevant to marketing, such as age, gender, interests and spending habits.

Customer segmentation relies on identifying key differentiators that divide customers into groups that can be targeted. Information such as a customer's: 

- Demographics (age, race, religion, gender, family size, ethnicity, income, education level)
- Geography (where they live and work)
- Psychographic (social class, lifestyle and personality characteristics) 
- Behavioral (spending, consumption, usage and desired benefits) tendencies 
are taken into account when determining customer segmentation practices.

In this Data Tale we will focus on behavioral Tendencies in order to group Customers into the following categories:
- Loyal Customers
- Best Customers
- Big Spenders Customers
- High Breadth Customers(those who buy a large range of products)
- Almost Lost Customers
- Lost Customers
- Lost Cheap Customers


#### RFM Metrics:
These stand for Recency,Frequency and Monetary metrics and they are widely used by organisations for behavioral segementation of their customers.

#### Recency
- How long ago was last purchase? (in no of days)
- Measured for “As Of Date” of data set which is taken as max(Invoice_Date) in our dataset

#### Frequency
- How many orders in analysis period?
- Attempting to measure engagement

#### Monetary
- What is total monetary value of all orders in analysis period?

Now I have also introduced Breadth as a metric in our analysis which is defined below:-

#### Breadth
- How many different kinds of products were purchased by the customer?

Hence our metrics can be termed as **RFMB Metrics**
## Defining Segments of Customers on the basis of RFM Metrics

### **Best Customers**
#### The best ones are in the first quartile in all R,F,M and B metrics

### **Loyal Customers**
#### The loyal customers are those who buy from us frequently or in first quartile of frequency metrics

### **Big Spender Customers**
#### The big spenders are those who are in first quartile of monetary metrics

### **High Breadth Customers**
#### The customers who buy a large range of products.

### **Almost Lost Customers**
#### The almost lost ones are in the third quartile of recency category

### **Lost Customers**
#### The lost ones are in the fourth quartile of recency category who used to buy frequently from us and we had monetary benefits from them

### **Lost Cheap Customers**
#### They are in the fourth quartile of all categories

## RFMB MARKETING STRATEGY
**The following strategies are recommended for rfmb:**
    <br>
    **BEST CUSTOMERS**: no price incentives, new products, and loyalty programs
    <br>
    **LOYAL CUSTOMERS**: Use frequency and monetary metrics to segment further
    <br>
    **BIG SPENDERS**: Market the most expensive products
    <br>
    **ALMOST LOST & LOST**: Aggresive price incentives
    <br>
    **LOST CHEAP CUSTOMERS**: Don't spend too many resources trying to acquire
    <br>
**To understand the complete analysis,open the ipynb notebook**    

