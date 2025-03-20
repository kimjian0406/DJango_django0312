# utils.py
from nltk.corpus import stopwords

def generate_tags_from_content(content):
    stop_words = set(stopwords.words('english'))
    words = content.split()
    tags = [word for word in words if word.lower() not in stop_words]
    return tags

