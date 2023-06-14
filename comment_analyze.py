from transformers import AutoTokenizer, AutoModelForSequenceClassification
from konlpy.tag import Okt
import torch


def analyze_comment(comments):
    tokenizer = AutoTokenizer.from_pretrained("checkpoint-9500")
    model = AutoModelForSequenceClassification.from_pretrained("checkpoint-9500")

    result = []

    for comment in comments:
        sentence, number = comment

        inputs = tokenizer.encode_plus(sentence, return_tensors='pt')
        outputs = model(**inputs)

        _, preds = torch.max(outputs.logits, dim=1)

        sentiment = 1 if preds[0].item() == 1 else -1

        result.append((sentence, number, sentiment))

    print(result)
    return result
