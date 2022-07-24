
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

![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/main/images/t5.jpg)

#### Training

1)Tokenizing texts using T5 tokenizer

2)Configuring the model

3)Train model


#### Evaluation Metrics 

1)BLEU (bilingual evaluation understudy)
Bleu measures precision: how much the words (and/or n-grams) in the machine generated summaries appeared in the human reference summaries.
BLEU works by computing the precision — the fraction of tokens from the candidate that appear, or are “covered”, by the references— but with a twist. Like any precision-based metric, the value of the BLEU score is always a number between 0 (worst) and 1 (best). BLEU  penalizes words that appear in the candidate more times than it appears in any of the references.
Eqtn:

![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/main/images/bleu_eqn.png)


Total : It’s the number of words in the candidate.
Covered : The total number of covered words.

For each unique word w, the number of words in the candidate is D(w)(count of candidate word w in candidate sentence), but the coverage is limited by R(w). So if D(w)≤R(w)(count of candidate  word w in reference sentences), all D(w) words are covered. Otherwise only R(w) words are covered. The number of covered words for each unique word w can simply be written as MIN(R(w), D(w)) where MIN is the minimum of the two values.



2)ROUGE:ROUGE stands for Recall-Oriented Understudy
 Rouge measures recall: how much the words (and/or n-grams) in the human reference summaries appeared in the machine generated summari. We can compute the precision and recall using the overlap.

Recall (in the context of ROUGE) refers to how much of the reference summary the system summary is recovering or capturing. If we are just considering the individual words, it can be computed as:
![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/main/images/recall.png)


In terms of precision, what you are essentially measuring is, how much of the system summary was in fact relevant or needed? Precision is measured as:

![alt text](https://raw.githubusercontent.com/vivekalex61/summary_creator/main/images/precision.png)


ROUGE-N, ROUGE-S, and ROUGE-L can be thought of as the granularity of texts being compared between the system summaries and reference summaries.

ROUGE-N — measures unigram, bigram, trigram and higher order n-gram overlap

ROUGE-L — measures longest matching sequence of words using LCS. An advantage of using LCS is that it does not require consecutive matches but in-sequence matches that reflect sentence level word order. Since it automatically includes longest in-sequence common n-grams, you don’t need a predefined n-gram length.

ROUGE-S — Is any pair of words in a sentence in order, allowing for arbitrary gaps. This can also be called skip-gram concurrence. For example, skip-bigram measures the overlap of word pairs that can have a maximum of two gaps in between words. As an example, for the phrase “cat in the hat” the skip-bigrams would be “cat in, cat the, cat hat, in the, in hat, the hat”.

could use the F1 measure to make the metrics work together: F1 = 2 * (Bleu * Rouge) / (Bleu + Rouge)

ref : https://towardsdatascience.com/nlp-metrics-made-simple-the-bleu-score-b06b14fbdbc1 , https://www.freecodecamp.org/news/what-is-rouge-and-how-it-works-for-evaluation-of-summaries-e059fb8ac840/ , https://stackoverflow.com/questions/9879276/how-do-i-evaluate-a-text-summarization-tool


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
