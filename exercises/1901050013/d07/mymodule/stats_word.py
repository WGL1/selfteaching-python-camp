import re
def stats_text_en(text):
    """Count the English words in the text."""
    text1 = re.sub('[^A-Za-z]',' ',text) # Remove the non-English characters in the text.
    text2 = text1.split() # Convert the string type to the list type.
    dict = {x: text2.count(x) for x in text2} # Count the times of each word in the list.
    dict1= sorted(dict.items(), key= lambda d:d[1], reverse = True) # Sort the words in the descending order according to the times of words.
    print(dict1) # Return the result.

    
def stats_text_cn(text):
    """Count the Chinese characters in the text."""
    text1 = re.sub('[A-Za-z.。，,、：“” ‘’ ?？!！「」\n-]','',text)  # Remove the non-Chinese characters in the text.
    text2 = list(text1) # Convert the string type to the list type.
    dict = {x: text2.count(x) for x in text2} # Count the times of each character in the list.
    dict1= sorted(dict.items(), key= lambda d:d[1], reverse = True) # Sort the character in the descending order according to the times of characters.
    print(dict1) # Return the result. 



def stats_text(text):
    """Count the English and Chinese characters in the text."""
    return(stats_text_en(text),stats_text_cn(text))


text = 'Python is so powerful and useful!自学是门手艺!自学能力非常重要!'
stats_text(text)

