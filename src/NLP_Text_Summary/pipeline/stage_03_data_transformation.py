
from src.NLP_Text_Summary.config.configuration import ConfigurationManager
from src.NLP_Text_Summary.conponents.data_transformation import DataTransformation
from transformers import AutoTokenizer

class DataTransformationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")

        self.data_transformation_config = self.config.get_data_transformation_config()
        self.data_transformation = DataTransformation(config=self.data_transformation_config, tokenizer=tokenizer)
        

    def main(self):
        self.data_transformation.initiate_data_transformation()






