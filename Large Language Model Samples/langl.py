# We will define the basics of the file that is to get hugging face
from transformers import LayoutLMForSequenceClassification, LayoutLMTokenizer
from torch.utils.data import DataLoader, SequentialSampler, TensorDataset
import torch
# Call the model
model = LayoutLMForSequenceClassification.from_pretrained('microsoft/layoutlm-base-uncased')
tokenizer = LayoutLMTokenizer.from_pretrained('microsoft/layoutlm-base-uncased')
# Seeing your files
with open(r'C:\Users\NamanJain\Downloads\_Stoic Philosophy, Stoicism.pdf', 'rb') as f:
    file_content = f.read()
# Convert the file to a list of strings, with one string per line
file_lines = file_content.decode('utf-8').split('\n')
#Tokenise the files to be able to easily be modelize
tokenized_lines = [tokenizer.encode(line, add_special_tokens=True) for line in file_lines]
# Set the token usable
max_length = 512

padded_lines = torch.zeros(len(tokenized_lines), max_length, dtype=torch.long)

for i, line in enumerate(tokenized_lines):
    padded_lines[i, :len(line)] = torch.tensor(line[:max_length])

input_ids = padded_lines[:, :max_length]

attention_mask = torch.where(input_ids != 0, torch.tensor(1), torch.tensor(0))

dataset = TensorDataset(input_ids, attention_mask)
device = torch.device('cpu')

model.eval().to(device)

batch_size = 8

sampler = SequentialSampler(dataset)

dataloader = DataLoader(dataset, sampler=sampler, batch_size=batch_size)

predictions = []

for batch in dataloader:
    batch = tuple(t.to(device) for t in batch)

    inputs = {'input_ids': batch[0],
              'attention_mask': batch[1]}

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs[0]

    batch_predictions = torch.argmax(logits, dim=1).tolist()

    predictions += batch_predictions

# Convert the predicted labels back to strings

predicted_labels = [tokenizer.decode(prediction) for prediction in predictions]
# the json file where the output must be stored 
import json
out_file = open("myfile.json", "w") 
    
json.dump(predicted_labels, out_file, indent = 6) 
