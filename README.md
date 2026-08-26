You used PyTorch mostly at a low level for your SLM, so several higher-level modules could have simplified parts of it:

torch.nn.TransformerEncoder / TransformerEncoderLayer — would replace much of your manual transformer block work (self-attention, feed-forward layers, residual connections, and LayerNorm).

torch.nn.MultiheadAttention — would replace your custom Q/K/V attention implementation and masking logic.

torch.nn.Transformer — a full encoder-decoder transformer if you needed both sides.

torch.nn.functional.pad — useful for handling variable-length sequences and padding instead of manually managing some shapes.

torch.utils.data.DataLoader + a custom Dataset — you likely used DataLoader, but a cleaner Dataset abstraction could simplify tokenization, batching, and sequence sampling.

torch.nn.CrossEntropyLoss — likely what you used for next-token prediction, but PyTorch also supports things like ignore_index to automatically ignore PAD tokens.

torch.optim.AdamW — a standard optimizer for transformers with weight decay handled correctly.

torch.nn.Embedding — you already used this, but it is the standard replacement for manually managing token embeddings.

torch.nn.LayerNorm — if you implemented normalization manually, this would remove that complexity.

torch.nn.Dropout — standard transformer regularization.

The biggest simplifications would have been nn.MultiheadAttention and nn.TransformerEncoderLayer. However, writing them yourself was actually useful because it forced you to understand attention, masking, embeddings, and residual connections instead of hiding them behind PyTorch.
