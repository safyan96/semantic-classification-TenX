from fastapi import APIRouter, Depends, Request
from src import SentenceEmbedder
from schemas import SentenceSimilarity, SimilarSentencesResponse

router = APIRouter(
    prefix="/query",
    tags=["classifier"],
    # dependencies=Depends(get_db),
    responses={404: {"description": "not found"}},
)
embedder = SentenceEmbedder("src/model")


@router.post("")
def query(config: SentenceSimilarity, request: Request):
    sentence, options = config.sentence, config.labels
    response = embedder.compare_sentence_embeddings(
        query_sentence=sentence, sentences=options
    )
    return response[0][0]


@router.post("/details")
def query_detail(config: SentenceSimilarity, request: Request):
    sentence, options = config.sentence, config.labels
    response = embedder.compare_sentence_embeddings(
        query_sentence=sentence, sentences=options
    )
    return response
