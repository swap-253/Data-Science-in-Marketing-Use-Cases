## Problem Statement
In this Project, I have worked upon creating content for our customers. Now I didn't have the marketing content data.
Hence I used a dataset consisting of lyrics of Taylor Swift's songs but that's relatable, isn't it? We are going to use the same stuff in automated marketing content creation too. .

The flow of this Analysis will be:
- First I have imported the dataset of lyrics of Taylor Swift's songs and created a corpus consisting of sentences. 

- **Data Preprocessing**:- Elimination of white spaces, alphanumeric characters, and end of a sentence or next sentence 

- **Tokenization**:-We then fit the tokenizer on our corpus and store the data related to corpus in tokenizer itself, so now each word has an index starting from 1.

- From there we get input sequences on the basis of numerical arrangement of order of words.

- **Model Building**:-We made it as a supervised learning problem, labels are predicted using predictors andd built a model consisting of embedding layer for word embeddings, Bidirectional LSTM, LSTM and Dense Layer

- In the Last step, content is predicted using our two functions which are **get_content** and **create_content** and all of these steps have been explained.

Open the notebook to get complete description of each of the steps

