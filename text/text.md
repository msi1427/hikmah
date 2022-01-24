# Using the functions in the text folder

## hikmah.text.transform

### processing

1. Import the library 

   ````python
   from hikmah.text.transform import processing
   ````

2. **processing_pipeline(data:list, pipeline:list)**

   ```python
   data = processing.processing_pipeline(<list of text>,<list of actions in sequence>)
   '''
   Example
   classes = processing.processing_pipeline(data=classes, pipeline=["normalize and","lowercase"])
   The 'classes' list will first 'normalize and' and them 'lowercase' the list of text
   '''
   ```

   ***list of actions available:***

   - `normalize whitespaces` : if there are more than one whitespaces consequentially, it will be reduced to just one.
   - `lowercase` : the alphabets will be lowercase if they are in 'uppercase'.
   - `normalize and` : replaces `&` and `&amp` to `and`.
   - `remove newlines` : removes `\n`, `\r` and `<br/>`.
   - `remove emoji` : removes [emojis](https://pypi.org/project/emoji/).
   - `remove urls` : removes urls starting with `http\S+`.
   - `remove hashtags` : removes hashtags.
   - `remove mentions` : removes mentions starting with `@`.
   - `remove punctuations` : removes `'''!()-[]{};:'"\,<>./?@#$%^&*_~'''` 
   - `remove stopwords` : removes defined [nltk](https://www.nltk.org/) stopwords.
   - `keep only alphanumeric` : keeps the alpha-numeric characters only `A-Z,a-z,0-9`

3. **normalize_whitespaces(text:str)** 

   ```python
   text = processing.normalize_whitespaces(text)
   # Returns text with normalized whitespaces
   ```

4. **remove_emoji(text:str)** 

   ```python
   text = processing.remove_emoji(text)
   # Returns processed text without emojis
   ```

5. **remove_punctuations(text:str)** 

   ```python
   text = processing.remove_punctuations(text)
   # Returns processed text without punctuations
   ```

6. **remove_emoji(text:str)** 

   ```python
   text = processing.remove_emoji(text)
   # Returns processed text without emojis
   ```

7. **remove_stopwords(text:str)** 

   ```python
   text = processing.remove_stopwords(text)
   # Returns processed text without any stop words
   ```

8. **keep_only_alphanumeric(text:str)** 

   ```python
   text = processing.keep_only_alphanumeric(text)
   # Returns processed text with only alphanumeric characters
   ```