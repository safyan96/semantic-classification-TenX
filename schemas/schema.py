from typing import List, Dict
from pydantic import BaseModel


class SentenceSimilarity(BaseModel):
    sentence: str
    labels: List[str]


class SimilarSentencesResponse(BaseModel):
    sentence: str
    similar_sentences: Dict
