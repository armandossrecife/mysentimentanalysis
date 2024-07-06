from transformers import DistilBertForSequenceClassification, AutoTokenizer
from datasets import load_dataset
from transformers import TrainingArguments, Trainer  # Import from transformers

# Define model name and task
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
task = "sentiment-analysis"

# Load pre-trained DistilBERT model and tokenizer
model = DistilBertForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the IMDB movie review dataset
train_data = load_dataset("imdb", split="train")
test_data = load_dataset("imdb", split="test")

# Function to preprocess text data
def preprocess_function(examples):
  return tokenizer(examples["text"], padding="max_length", truncation=True)

# Preprocess train and test data
train_data = train_data.map(preprocess_function, batched=True)
test_data = test_data.map(preprocess_function, batched=True)

#mkdir results

training_args = TrainingArguments(
    output_dir="results",  # Fixed typo (removed extra space)
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=16,  # Assuming you meant "size" here
    learning_rate=2e-5,
)

# Create trainer object
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
    compute_metrics="accuracy",
)

print("Aguarde o treinamento do modelo...")
# Train the model
trainer.train()

# Predict sentiment for a new review 
new_review = "This movie was amazing! Highly recommend."
inputs = tokenizer(new_review, padding="max_length", truncation=True, return_tensors="pt")
with torch.no_grad():
  outputs = model(**inputs)
predictions = torch.argmax(outputs.logits, dim=-1)

# Print the predicted sentiment
if predictions == 1:
  print("Sentiment: Positive")
else:
  print("Sentiment: Negative")

