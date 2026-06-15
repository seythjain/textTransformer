# In this model the tokens are words
# there are 100 words
# the embedding space is 32

import torch
import torch.nn as nn
import math
from torch.utils.data import Dataset, DataLoader
from wordIds import vocab

train = True



num_words = 99 # 99 words + PAD token

# must add one because we need to account for the padding token
num_tokens = num_words + 1  # PAD token included

embedding_dim = 32

emb = torch.nn.Embedding(num_tokens, embedding_dim)

max_seq_len = 512  # safe upper bound for now
pos_emb = torch.nn.Embedding(max_seq_len, embedding_dim)

# loss fn
criterion = nn.CrossEntropyLoss()

# the number of scentences we do training on in parallel
batch_size = 8



def assignIds(words):
    out = []

    wordIds = vocab

    for word in words:
        out.append(wordIds[word])

    return out


def collate_fn(batch):
    inputs, targets = zip(*batch)
    
    max_len = 0
    for i in inputs:
        max_len = max(max_len, len(i))

    inputs_padded = []
    # make sure that inputs is a rectangle
    for i in range(len(inputs)):
        inp = []
        for j in inputs[i]:
            inp.append(j)

        for _ in range(max_len-len(inputs[i])):
            inp.append(vocab["<PAD>"])

        inputs_padded.append(inp)

    targets = torch.tensor(targets)

    
    inputs_padded = torch.tensor(inputs_padded)
    
    return inputs_padded, targets


# attention part
class SelfAttention(nn.Module):
    # create the query, key, value weight matricies
    #   nn.Linear creates a new weight matrix
    #   by calling it, the parameter/input (the embedding matrix) is multiplied by the weight matrix
    def __init__(self, emb_dim):
        super().__init__()
        self.Wq = nn.Linear(emb_dim, emb_dim)
        self.Wk = nn.Linear(emb_dim, emb_dim)
        self.Wv = nn.Linear(emb_dim, emb_dim)
        
        # linear layers
        self.fc1 = nn.Linear(emb_dim, 128)
        self.fc2 = nn.Linear(128, emb_dim)
        # relu function
        self.relu = nn.ReLU()

        # unembed to come up with a prediction
        self.unembed = nn.Linear(emb_dim, num_tokens) 

        self.emb_dim = emb_dim

    def forward(self, x):
        x = torch.nn.functional.layer_norm(x, (self.emb_dim,))

        # the query vectors
        Q = self.Wq(x)
        K = self.Wk(x)
        V = self.Wv(x)

        # all we are doing is the attention equation:
        # Attention(Q,K,V) = softmax( (Q @ K^T)/sqrt(emb_dim) ) @ V

        # multiply the K and Q vectors to create a grid of correlations between them for all tokens
        #    K E Y
        # Q  tokens    i->
        # U  j   |Q1@K1 | Q1@K2 | Q1@K3 | Q1@K4  .  .  .
        # E  ↓   |Q2@K1 | Q2@K2 | Q2@K3 | Q2@K4  .  .  .
        # R      |Q3@K1 | Q3@K2 | Q3@K3 | Q3@K4  .  .  .
        # Y      |Q4@K1 | Q4@K2 | Q4@K3 | Q4@K4  .  .  .
        #           .       .       .       .
        #           .       .       .       .
        #           .       .       .       .
        # Each of these dot products (Q_i @ K_i) computes the correlation between the vectors Q_i and K_i
        # Q_i @ K_i = |Q_i||K_i|cos(theta) where theta = the (smaller) angle between the two vectors in the high dim space

        scores = Q @ K.transpose(-2, -1)
        
        # normalize the values to make sure the softmax function doesnt go crazy (idk why this helps/works, but we are just multiplying a scalar and matrix)
        # ChatGPT says:
        # Because:
        #   dot products grow with dimension size
        #   large values make softmax unstable
        # So we normalize to keep training stable.

        scores /= math.sqrt(self.emb_dim)

        # apply masking and basically ignore anything thats a padding token
        #   this ensures the model can only look at current and past tokens
        T = scores.shape[-1]
        mask = torch.tril(torch.ones(T, T, device=scores.device))
        mask = mask.masked_fill(mask == 0, float('-inf'))

        # FIX: actually apply mask
        scores = scores.masked_fill(mask == 0, float('-inf'))

        # pretty simple, apply softmax function
        weights = torch.softmax(scores, dim=-1)

        out = weights @ V
        # add residual 
        #   the output = orig meaning + newly discovered meaning
        x = x + out
        x = torch.nn.functional.layer_norm(x, (self.emb_dim,))

        mlp_out = self.fc1(x)
        mlp_out = self.relu(mlp_out)
        mlp_out = self.fc2(mlp_out)

        x = x + mlp_out

        # take last token for prediction
        x = x[:, -1, :]   # (B, 32)

        logits = self.unembed(x)   # (B, vocab_size)

        return logits


# instance of the model
attn = SelfAttention(embedding_dim)    

optimizer = torch.optim.Adam(attn.parameters(), lr=1e-3)

inv_vocab = {v: k for k, v in vocab.items()}

if train:
    
    # data takes the scentences in train.txt and puts them into:
    # [
    #   [word, word, word, ...]
    #   [word, word, word, ...]
    #   [word, word, word, ...]
    #       .
    #       .
    #       .
    # ]

    # len(data) = 2**18 as defined in scentenceGen.py
    data = [line.split() for i,line in enumerate(open("train.txt", "r").readlines()) if i % 2 == 0]

    dataset = []

    for example in data:
        # example is a scentence
        # EX: ["i", "like", "ml"]

        ids = assignIds(example)

        # each entry in dataset will be (input, target)
        # an example dataset = [
        #   (["i"], "like")
        #   (["i", "like"], "ml")
        # ]

        for i in range(len(ids) - 1):
            dataset.append((ids[:i+1], ids[i+1]))


    class NextWordDataset(Dataset):
        def __init__(self, data):
            self.data = data

        def __len__(self):
            return len(self.data)

        def __getitem__(self, idx):
            return self.data[idx]


    ds = NextWordDataset(dataset)

    loader = DataLoader(ds, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)

    for inputs, targets in loader:
        logits = attn(inputs)

        loss = criterion(logits, targets)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        print(loss.item())

else:
    prompt = input("Enter a prompt: ")
    prompt = prompt.split()

    num_new_words = int(input("Enter an integer number of new words to finish prompt: "))

    # switch model to inference mode
    attn.eval()

    # convert prompt into ids (DO THIS ONCE, NOT EACH LOOP)
    x = torch.tensor([[vocab[w] for w in prompt]])

    print(" ".join(prompt), end=" ")

    for _ in range(num_new_words):
        # stops gradients from being tracked
        with torch.no_grad():

            # forward pass
            logits = attn(x)

            # probability distribution
            probs = torch.softmax(logits, dim=-1)

            # greedily choose highest probability
            next_id = torch.argmax(probs, dim=-1)

            # convert tensor to int
            next_word = next_id.item()

            # append to sequence
            x = torch.cat([x, next_id.unsqueeze(0)], dim=1)

            # print generated word
            print(inv_vocab[next_word], end=" ")