from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


def analyzeTendencyComment(comments):
    tokenizer = AutoTokenizer.from_pretrained("checkpoint-9500")
    model = AutoModelForSequenceClassification.from_pretrained("checkpoint-9500")

    result = []

    positive = 0

    for comment in comments:
        sentence, number = comment

        inputs = tokenizer.encode_plus(sentence, return_tensors='pt')

        outputs = model(**inputs)

        _, pre = torch.max(outputs.logits, dim=1)

        sentiment = 1

        if pre[0].item() == 1:
            positive += 1
        else:
            sentiment = -1

        result.append((sentence, number, sentiment))

    percent = positive/len(comments)

    return percent, result
