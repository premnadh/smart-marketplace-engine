from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_items(items, target_item_id, top_n=3):

    # combine text features
    texts = [
        f"{item.title} {item.description} {item.category}"
        for item in items
    ]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(tfidf_matrix)

    target_index = None

    for i, item in enumerate(items):
        if item.id == target_item_id:
            target_index = i
            break

    if target_index is None:
        return []

    scores = list(enumerate(similarity[target_index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for idx, score in scores[1:top_n+1]:
        recommendations.append(items[idx])

    return recommendations