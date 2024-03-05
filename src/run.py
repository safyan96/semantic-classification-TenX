from transformer.infer import SentenceEmbedder

if __name__ == "__main__":
    # Initialize SentenceEmbedder with the model name
    embedder = SentenceEmbedder("model")

    # Sentences we want sentence embeddings for
    query_sentence = ["feeling like a million bucks"]

    # Query sentence
    options = ["Happy", "Sad", "Rich"]

    # Get most similar sentences to the query sentence
    similar_sentences = embedder.compare_sentence_embeddings(query_sentence, options)

    # Print most similar sentences
    print("Most similar sentences to '{}':".format(query_sentence))
    for sentence, similarity in similar_sentences:
        print("- {} (Cosine similarity: {})".format(sentence, similarity))
