
from src.NLP_Text_Summary.config.configuration import ConfigurationManager
from src.NLP_Text_Summary.conponents.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.data_ingestion_config = self.config.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(config=self.data_ingestion_config)
    
    def start_data_ingestion(self):
        self.data_ingestion.download_file()
        self.data_ingestion.extract_zip_file()

 