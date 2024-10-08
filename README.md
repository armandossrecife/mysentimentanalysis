# mysentimentanalysis

My Sentiment Analysis. 

This code explores the application of sentiment analysis to the [IMDB movie](https://www.imdb.com/) based on the reviews from the this [dataset](https://huggingface.co/datasets/mteb/imdb). It leverages a pre-trained DistilBERT model to automatically classify movie reviews as positive or negative based on their text content.

[How it workds?](https://github.com/armandossrecife/mysentimentanalysis/blob/main/HowItWorks.md)

Enable GPU in your machine. 

**Install the dependencies**:

Install [requirements](https://github.com/armandossrecife/mysentimentanalysis/blob/main/requirements.txt).

**Create the folder results**:

```bash
mkdir results
```

**Running this example**: 

```bash
python3 main.py
```

**Input/Output**

Input:
```bash
new_review = "This movie was amazing! Highly recommend."
```

Ouput:
```bash
entiment: Positive
```

**Using the Google Colabs to try this example**: 

You can try this [notebook](https://github.com/armandossrecife/mysentimentanalysis/blob/main/my_sentiment_analysis.ipynb).
