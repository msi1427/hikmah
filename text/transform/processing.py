import imp
import emoji
import re
import nltk
from tqdm import tqdm

nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

def normalize_whitespaces(text:str):
    '''
    Params:
        text : raw text
    Returns:
        processed text
    '''
    text = " ".join(text.split())
    return text

def processing_pipeline(data:list, pipeline:list = []):
    '''
    Params:
        data : list of text
        pipeline : processing pipeline in sequence as list
    Returns:
        processed list of text
    '''
    for action in tqdm(pipeline):
        
        if action == "normalize whitespaces":
            data = [normalize_whitespaces(text) for text in data]
        
        if action == "lowercase":
            data = [text.lower() for text in data]
        
        if action == "normalize and":
            data = [re.sub("&", "and", text) for text in data]
            data = [re.sub("&amp", "and", text) for text in data]

    return data