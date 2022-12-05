import json
from pickletools import optimize
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np
from model import ChatNeuralNet

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

with open('../sas_chat_bot/edudataset.json', 'r') as json_data:
    dataset = json.load(json_data)

all_words = []
tags = []
bc = []

for data in dataset['intents']:
    tag = data['tag']
    tags.append(tag)
    for pattern in data['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        bc.append((w, tag))

ignore_words = ['?', '!', '.', ',', ':', ';', '-']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

A_train = []
b_train = []

for (pattern_sentence, tag) in bc:
    bag = bag_of_words(pattern_sentence, all_words)
    A_train.append(bag)

    label = tags.index(tag)
    b_train.append(label)

A_train = np.array(A_train)
b_train = np.array(b_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(A_train)
        self.a_data = A_train
        self.b_data = b_train

    def __getitem__(self, index):
        return self.a_data[index], self.b_data[index]

    def __len__(self):
        return self.n_samples

batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(A_train[0])
learning_rate = 0.001
num_epochs = 1000

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = ChatNeuralNet(input_size, hidden_size, output_size).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        output = model(words)
        loss = criterion(output, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch: {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}')

print(f'Final loss, Loss: {loss.item():.4f}')

data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    "output_size": output_size,
    "all_words": all_words,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)
print(f'Training complete. Saved model to {FILE}')