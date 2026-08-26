# Small Language Model

A small language model built from scratch in **PyTorch** to explore how Transformer-based language models work.
The goal is to build and show the core components of a language model rather than maximize performance. The model aims to use the torch.nn module as little as possible, to show how a transformer works.

## Features

* Word-level tokenization
* Learned word embeddings
* Positional embeddings
* Causal self-attention
* Transformer architecture
* Residual connections and LayerNorm
* Next-token prediction
* Training and text generation

## Goal

This project is primarily an educational implementation for displaying the fundamentals of Transformers and small language models.

## Tech
### This model does not utilize many of the higher level torch.nn modules.
####Examples:
  * nn.MultiheadAttention — would replace your manual Q/K/V projections, attention scores, masking, and head splitting.
  * nn.TransformerEncoderLayer — would provide an entire Transformer block, including attention, feed-forward layers, residual connections, and normalization.
  * nn.TransformerEncoder — would stack Transformer blocks for you.
  * nn.Dropout — helps reduce overfitting and is commonly used in Transformer models.

* Python
* PyTorch

## Status

Experimental — the model is intentionally small and is mainly intended for learning and experimentation. Although the model's training loop theoreticallly works, it needs some actual data to train on.
