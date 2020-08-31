import re
import string

def preprocess(text):
    def removeUnicode(text):
        text = re.sub(r'(\\u[0-9A-Fa-f]+)', r'', text)
        text = re.sub(r'[^\x00-\x7f]', r'', text)
        return text

    def replaceURL(text):
        text = re.sub(
            '((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', '', text)
        text = re.sub(r'#([^\s]+)', r'\1', text)
        return text

    def replaceAtUser(text):
        text = re.sub('@[^\s]+', '', text)
        return text
    def removeHashtagInFrontOfWord(text):
        """ Removes hastag in front of a word """
        text = re.sub(r'#([^\s]+)', "r'\1'", text)
        return text
    def removeNumbers(text):
        """ Removes integers """
        text = ''.join([i for i in text if not i.isdigit()])
        return text
    def removeEmoticons(text):
        """ Removes emoticons from text """
        text = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|:p|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', '', text)
        return text
    def remove_punct(text):
        text = "".join([char for char in text if char not in string.punctuation])
        text = re.sub('[0-9]+', '', text)
        text = re.sub(r"http\S+", "", text)
        return text
    def removeEscapeCharacter(text):
        pattern = re.compile(r'[\n\r\t]')
        text = pattern.sub(' ', text)
        return text
    text = replaceURL(text)
    text = removeEmoticons(text)
    text = text.lower()
    text = removeUnicode(text)
    text = replaceAtUser(text)
    text = removeHashtagInFrontOfWord(text)
    text = removeNumbers(text)
    text = re.sub('(pic.[^\s]+)', '', text) #remove pic. url
    text = remove_punct(text)
    text = removeEscapeCharacter(text)
    return text
def prep(sent):
    return preprocess(sent)
