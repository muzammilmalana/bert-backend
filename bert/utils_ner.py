from transformers import pipeline, AutoTokenizer
from typing import List, Tuple

def get_bio_tags(text, entities, tokenizer):
    tokens = tokenizer.tokenize(text)
    labels = ['O'] * len(tokens)
    offsets = tokenizer(text, return_offsets_mapping=True, truncation=True)['offset_mapping']
    for ent in entities:
        start, end, label = ent['start'], ent['end'], ent['entity_group']
        entity_started = False
        for i, (s, e) in enumerate(offsets):
            if s == e == 0:
                continue
            if s >= start and e <= end:
                if not entity_started:
                    if(labels[i-1] == 'O'):
                        labels[i-1] ='B-' + label
                        entity_started = True
                else:
                    labels[i-1] = 'I-' + label
    return tokens, labels

def make_predictions(texts: List[str]) -> Tuple[List[str], List[str]]:
    ner_pipeline = pipeline('ner', model='CyberPeace-Institute/SecureBERT-NER', grouped_entities=True)
    tokenizer = AutoTokenizer.from_pretrained("CyberPeace-Institute/SecureBERT-NER")
    tokens = []
    pred_labels = []
    for txt in texts:
        pred_ent = ner_pipeline(txt)
        tkns, pred_lbels = get_bio_tags(txt, pred_ent, tokenizer)
        tokens.extend(tkns)
        pred_labels.extend(pred_lbels)
    return tokens, pred_labels 