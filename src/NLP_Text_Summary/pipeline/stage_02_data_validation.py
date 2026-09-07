
from src.NLP_Text_Summary.config.configuration import ConfigurationManager
from src.NLP_Text_Summary.conponents.data_validation import DataValiadtion

class DataValidationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.data_validation_config = self.config.get_data_validation_config()
        self.data_validation = DataValiadtion(config=self.data_validation_config)

    def main(self):
        self.data_validation.validate_all_files_exist()
        
 