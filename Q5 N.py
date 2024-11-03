from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running", "jumps", "easily", "fairly"]
stemmed_words = [ps.stem(word) for word in words]
print(stemmed_words)
