
import os
import urllib.request as request
from datasets import load_dataset, load_from_disk

from src.NLP_Text_Summary.logging import logger
from pathlib import Path
from src.NLP_Text_Summary.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config, tokenizer):
        self.config = config
        # 1. MAKE SURE THIS LINE EXISTS AND IS RUNNING
        self.tokenizer = tokenizer 

    def convert_examples_to_features(self, example_batch):
        # 2. This will now successfully find self.tokenizer
        input_encodings = self.tokenizer(
            example_batch['dialogue'], 
            max_length=1024, 
            truncation=True
        )
        
        target_encodings = self.tokenizer(
            example_batch['summary'], 
            max_length=128, 
            truncation=True
        )
        
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def initiate_data_transformation(self):
        # Example dataset mapping call
        dataset = load_from_disk(self.config.data_path)
        dataset_pt = dataset.map(self.convert_examples_to_features, batched=True)
        dataset_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))

 