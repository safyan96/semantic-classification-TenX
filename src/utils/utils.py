import torch
import torch.nn.functional as F
import numpy as np


def mean_pooling(model_output, attention_mask):
    """
    Perform mean pooling on the token embeddings given the attention mask.

    Args:
    - model_output (tuple of torch.Tensor): Output of the model, typically containing token embeddings.
    - attention_mask (torch.Tensor): Attention mask to mask out padded tokens.

    Returns:
    - torch.Tensor: Mean-pooled embedding.
    """
    token_embeddings = model_output[
        0
    ]  # First element of model_output contains all token embeddings
    input_mask_expanded = (
        attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    )
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
        input_mask_expanded.sum(1), min=1e-9
    )


def cosine_similarity(vec1, vec2):
    """
    Compute the cosine similarity between two vectors using PyTorch functions.

    Args:
    - vec1 (torch.Tensor): The first vector.
    - vec2 (torch.Tensor): The second vector.

    Returns:
    - float: The cosine similarity between the two vectors.
    """
    cosine_sim = F.cosine_similarity(vec1, vec2, dim=-1)
    return cosine_sim.item()
