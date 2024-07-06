# mysentimentanalysis

My Sentiment Analysis. 

This code explores the application of sentiment analysis to the [IMDB movie](https://www.imdb.com/) based on the reviews from the this [dataset](https://huggingface.co/datasets/mteb/imdb). It leverages a pre-trained DistilBERT model to automatically classify movie reviews as positive or negative based on their text content.

[How it workds?](https://github.com/armandossrecife/mysentimentanalysis/blob/main/HowItWorks.md)

Enable GPU in your machine. 

```bash
python3 main.py
```

Input/Output

Input:
```bash
new_review = "This movie was amazing! Highly recommend."
```

Ouput:
```bash
entiment: Positive
```
