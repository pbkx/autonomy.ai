import pickle, os, sys, random, time, re, math, operator
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torch import nn, optim
from collections import *
import numpy as np
from numpy import dot
from numpy.linalg import norm
from datasets import load_dataset
from transformers import BertTokenizer
subword_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

task1_data = load_dataset('tweet_eval', 'irony')
task2_data = load_dataset('gsm8k', 'main')
task3_data = load_dataset('eli5_category')
lm_dataset = load_dataset('wikitext', 'wikitext-103-v1')
lm_dataset = lm_dataset['train'].filter(lambda e,i: i<20000, with_indices=True)

def train_ngram_lm(data):
    lm = defaultdict(Counter)
    count = 0
    for example in data:
      count += 1
      tokenized_sentence = subword_tokenizer.tokenize('[CLS] '+example['text']+' [SEP]')
      for i in range(1, len(tokenized_sentence)):
        # increment trigram: count(x_{i-2}, x_{i-1}, x_i)
        if i > 2: 
          lm[tokenized_sentence[i-2] + " " + tokenized_sentence[i-1]].update([tokenized_sentence[i]])
        # increment bigram: count(x_{i-1}, x_i)
        lm[tokenized_sentence[i-1]].update([tokenized_sentence[i]])
        # no context, increment unigram: count (x_i)
        lm[''].update([tokenized_sentence[i]])
      if count%2000==0:
        print('%d/20000 lines processed so far.' % count)
    # normalize to map counts into a probability distribution
    for _, v in lm.items():
      total = sum(v.values(), 0.0)
      for key in v:
        v[key] /= total
    return lm
# We train our model here!
lm = train_ngram_lm(lm_dataset)

lm[''].most_common(10)