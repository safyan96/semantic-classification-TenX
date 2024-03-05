from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from utils import cosine_similarity, mean_pooling

class SentenceEmbedder:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        
    def get_sentence_embeddings(self, sentences):
        # Tokenize sentences
        encoded_input = self.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
        
        # Compute token embeddings
        with torch.no_grad():
            model_output = self.model(**encoded_input)

        # Perform pooling
        sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

        # Normalize embeddings
        sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

        return sentence_embeddings

    def compare_sentence_embeddings(self, query_sentence, sentences):
        # Get embeddings
        query_embedding = self.get_sentence_embeddings(query_sentence)[0]
        embeddings = self.get_sentence_embeddings(sentences)
        
        # Calculate cosine similarities
        similarities = {}
        for idx, embedding in enumerate(embeddings):
            similarities[sentences[idx]] = cosine_similarity(query_embedding, embedding)

        # Sort similarities by score in descending order
        sorted_similarities = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
        
        return sorted_similarities

# Example usage
if __name__ == "__main__":
    # Initialize SentenceEmbedder with the model name
    embedder = SentenceEmbedder('model')
    
    # Sentences we want sentence embeddings for
    query_sentence = ["feeling like a million bucks"]
    
    # Query sentence
    options = ["Happy","Sad","Rich"]
    
    # Get most similar sentences to the query sentence
    similar_sentences = embedder.compare_sentence_embeddings(query_sentence, options)
    
    # Print most similar sentences
    print("Most similar sentences to '{}':".format(query_sentence))
    for sentence, similarity in similar_sentences:
        print("- {} (Cosine similarity: {})".format(sentence, similarity))
