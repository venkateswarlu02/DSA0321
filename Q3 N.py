import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Initialize Porter Stemmer and WordNet Lemmatizer
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def morphological_analysis(text):
    # Tokenize the input text
    words = word_tokenize(text)
    
    # Perform stemming and lemmatization
    stems = [ps.stem(word) for word in words]
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in words]  # 'v' for verb
    
    # Display results
    print(f"Original Words: {words}")
    print(f"Stemmed Words:  {stems}")
    print(f"Lemmatized Words: {lemmas}")

# Test the function with sample text
text = "running runs runner jumped jumping"
morphological_analysis(text)
