import emoji
import re
import nltk
from tqdm import tqdm

nltk.download('stopwords')
from nltk.corpus import stopwords

def normalize_whitespaces(text:str):
    '''
    Params:
        text : raw text
    Returns:
        processed text
    '''
    text = " ".join(text.split())
    return text

def remove_emoji(text:str):
    '''
    Params:
        text : raw text
    Returns:
        processed text without emojis
    '''
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
    return clean_text

def remove_punctuations(text:str):
    '''
    Params:
        text : raw text
    Returns:
        processed text without punctuations
    '''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in text:
        if char not in punctuations: 
            no_punct = no_punct + char
        else: no_punct = no_punct + ' '
    return no_punct

def remove_stopwords(text:str):
    '''
    Params:
        text : raw text
    Returns:
        processed text without any stop words
    '''
    stop_words = stopwords.words('english')
    text_tokens = text.split()
    tokens_without_sw = [word for word in text_tokens if not word in stop_words]
    filtered_sentence = (" ").join(tokens_without_sw)
    return filtered_sentence

def keep_only_alphanumeric(text:str): 
    '''
    Params:
        text : raw text
    Returns:
        processed text with only alphanumeric characters
    '''
    text = re.sub(r'[^A-Za-z0-9 ]+', ' ', text)
    return " ".join(text.split())

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
        
        if action == "remove newlines":
            data = [re.sub('\s+', ' ', sent) for sent in data]
            data = [re.sub('<br/>', ' ', sent) for sent in data]
        
        if action == "remove emoji":
            data = [remove_emoji(text) for text in data]
        
        if action == "remove urls":
            data = [re.sub('http\S+', " ", text) for text in data]
        
        if action == "remove urls":
            data = [re.sub('http\S+', " ", text) for text in data]
        
        if action == "remove hashtags":
            data = [re.sub('#\S+', " ", text) for text in data]
        
        if action == "remove mentions":
            data = [re.sub('@\S+', " ", text) for text in data]
        
        if action == "remove punctuations":
            data = [remove_punctuations(text) for text in data]
        
        if action == "remove stopwords":
            data = [remove_stopwords(text) for text in data]
        
        if action == "keep only alphanumeric":
            data = [keep_only_alphanumeric(sent) for sent in data]

    return data