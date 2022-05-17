
# Summary creator
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

Building a text summarizer using T5 transformer.

![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/main/images/intro.jpg)

## Introduction 

#### 
Text summarization is a way to condense the large amount of information into a concise form by the process of selection of important information and discarding unimportant and redundant information. With the amount of textual information present in the world wide web the area of text summarization is becoming very important. 
There are two types of summarization 

1)Extractive Summarization:

Extractive Summarization essentially involves extracting particular pieces of text (usually sentences) based on predefined weights assigned to the important words where the selection of the text depends on the weights of the words in it.

2)Abstractive Summarization:

Abstractive Summarization includes heuristic approaches to train the system in making an attempt to understand the whole context and generate a summary based on that understanding.

ref : https://medium.com/swlh/abstractive-text-summarization-using-transformers-3e774cc42453 

## Overview 
- Datasets and Data-Loading
- Data Preprocessing
- Model creation and training
- Recorder creation

### Datasets and Data-Loading
The dataset consists of 4515 examples and contains Author_name, Headlines, Url of Article, Short text, Complete Article. I gathered the summarized news from Inshorts and only scraped the news articles from Hindu, Indian times and Guardian. Time period ranges from febrauary to august 2017.
link : https://www.kaggle.com/datasets/pariza/bbc-news-summary


### Data Preprocessing

1)Data  Pre-processing includes removing of symbols  and emojis. 

2)Padding after tokenization

### Model building and training

#### 1)Model
T5 or Text-to-Text Transfer Transformer, is a Transformer based architecture that uses a text-to-text approach. Every task – including translation, question answering, and classification – is cast as feeding the model text as input and training it to generate some target text. This allows for the use of the same model, loss function, hyperparameters, etc. across our diverse set of tasks. The changes compared to BERT include:

1, adding a causal decoder to the bidirectional architecture.

2, replacing the fill-in-the-blank cloze task with a mix of alternative pre-training task

![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/tree/main/images/t5.jpg)

#### Training

1)Tokenizing texts using T5 tokenizer

2)Configuring the model

3)Train model

#### Deployment

1)The model is deployed as web application using FLASK

2)Web application is dockerised and uploaded to docker hub


## Results

Below are the results  got from trained transformer.



![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/main/images/pred1.png)

![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/main/images/pred2.png)

## How to use.

### Docker
Pull from docker using `docker pull vivekalex/summarize_app:latest`

Run `sudo docker run -p 5000:5000 vivekalex/summarize_app`

Copy the url `http://172.17.0.2:5000/`

![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/main/images/sum_home.png)

## End Notes
Model is trained on news summaries. It will perform well in news article summarization
