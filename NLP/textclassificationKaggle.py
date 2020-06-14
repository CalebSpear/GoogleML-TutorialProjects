# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:16:20 2020

@author: caleb
"""
import pandas as pd
import spacy
from spacy.util import minibatch
import random
from sklearn.model_selection import train_test_split
def load_data(csv_file, split=0.9):
    data = pd.read_csv(csv_file, encoding = "latin-1")
    data = data[['v1', 'v2']]
    data = data.rename(columns = {'v1': 'label', 'v2': 'text'})
    data["isSpam"] = data.label.map({"spam": 1, "ham": 0})
    
    # Shuffle data
    train_data = data.sample(frac=1, random_state=7)
    #train_data = data.head(10)
    texts = train_data.text.values
    labels = [{"spam": bool(y), "ham": not bool(y)}
              for y in train_data.isSpam.values]
    split = int(len(train_data) * split)
    
    train_labels = [{"cats": labels} for labels in labels[:split]]
    val_labels = [{"cats": labels} for labels in labels[split:]]
    
    return texts[:split], train_labels, texts[split:], val_labels

train_texts, train_labels, val_texts, val_labels = load_data('spam.csv')

# ham is the label for non-spam messages

# Create an empty model
nlp = spacy.blank("en")

# Create the TextCategorizer with exclusive classes and "bow" architecture
textcat = nlp.create_pipe(
              "textcat",
              config={
                "exclusive_classes": True,
                "architecture": "bow"})

# Add the TextCategorizer to the empty model
nlp.add_pipe(textcat)

# Add labels to text classifier
textcat.add_label("ham")
textcat.add_label("spam")

def train(model, train_data, optimizer):
    losses = {}
    random.seed(1)
    random.shuffle(train_data)
    
    batches = minibatch(train_data, size=8)
    for batch in batches:
        # train_data is a list of tuples [(text0, label0), (text1, label1), ...]
        # Split batch into texts and labels
        texts, labels = zip(*batch)
        
        # Update model with texts and labels
        model.update(texts, labels, sgd = optimizer, losses = losses)
        
    return losses

spacy.util.fix_random_seed(1)
random.seed(1)

optimizer = nlp.begin_training()
train_data = list(zip(train_texts, train_labels))

losses = train(nlp, train_data, optimizer)

def predict(model, texts): 
    # Use the model's tokenizer to tokenize each input text
    docs = [nlp.tokenizer(text) for text in texts]
    
    # Use textcat to get the scores for each doc
    textcat = nlp.get_pipe("textcat")
    scores, _ = textcat.predict(docs)
    
    # From the scores, find the class with the highest score/probability
    predicted_class = scores.argmax(axis=1)
    
    return predicted_class

def evaluate(model, texts, labels):
    """ Returns the accuracy of a TextCategorizer model. 
    
        Arguments
        ---------
        model: ScaPy model with a TextCategorizer
        texts: Text samples, from load_data function
        labels: True labels, from load_data function
    
    """
    # Get predictions from textcat model (using your predict method)
    predicted_class = predict(model, texts)
    
    # From labels, get the true class as a list of integers (POSITIVE -> 1, NEGATIVE -> 0)
    true_class = [int(each['cats']['spam']) for each in labels]
    
    # A boolean or int array indicating correct predictions
    correct_predictions = predicted_class == true_class
    
    # The accuracy, number of correct predictions divided by all predictions
    accuracy = correct_predictions.mean()
    
    return accuracy

n_iters = 5
for i in range(n_iters):
    losses = train(nlp, train_data, optimizer)
    accuracy = evaluate(nlp, val_texts, val_labels)
    print(f"Loss: {losses['textcat']:.3f} \t Accuracy: {accuracy:.3f}")