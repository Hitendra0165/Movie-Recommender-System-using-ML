## Project: Movie Recommender System Using Machine Learning!

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalized lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence-based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.


#Types of Recommendation Systems:

1.Content-Based:
Definition: Utilizes item attributes and user profiles to make recommendations.
Examples: Twitter, YouTube.
Key Feature: Forms embeddings for item features, creating a vector for recommendation based on user-specific actions or similar items.

2.Collaborative-Based:
Definition: Relies on user-item interactions and clusters of users with similar preferences.
Examples: Book recommendations.
Key Feature: Considers only one parameter, such as ratings or comments, assuming that users with similar preferences will like the same items.
Issues:

Computationally expensive due to a user-item nXn matrix.
Tends to recommend only famous items.
New items might not receive recommendations.

3.Hybrid-Based:
Definition: Combines content-based and collaborative-based approaches to address individual system limitations.
Key Use: Utilizes techniques like word2vec and embedding for enhanced recommendation accuracy.
Advantages: Mitigates issues present in content-based and collaborative-based systems.

# About this project:

This is a streamlit web application that can recommend various kinds of similar movies based on an user interest.
here is a demo,

* [Click here to run it live on server](https://movie-recommeder-system.herokuapp.com/)


# Demo:

<img src="demo/1.png" alt="workflow" width="70%">

<img src="demo/2.png" alt="workflow" width="70%">

<img src="demo/3.png" alt="workflow" width="70%">


# Dataset has been used:

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

# Concept used to build the model.pkl file : cosine_similarity

1 . Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3 . Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4 . It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

5 . For more details , check URL : https://www.learndatasci.com/glossary/cosine-similarity/

# How to run?
### STEPS:

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n movie python=3.7.10 -y
```

```bash
conda activate movie
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
#run this file to generate the models

Movie Recommender System Data Analysis.ipynb
```

Now run,
```bash
streamlit run app.py
```


```bash
Author: Hitendra Bhamare
Data Scientist
Email: hitendrabhamare007@gmail.com

```

