from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_ranking(documents, query):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    query_vec = vectorizer.transform([query])

    similarity = (tfidf_matrix * query_vec.T).toarray()
    ranked_docs = sorted(enumerate(similarity), key=lambda item: -item[1])
    return ranked_docs

documents = [
    "The cat sat on the mat",
    "The dog chased the cat",
    "The cat climbed a tree"
]
query = "cat"
print(tfidf_ranking(documents, query))
