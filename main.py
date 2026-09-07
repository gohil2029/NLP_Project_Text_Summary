from src.NLP_Text_Summary.logging import logger
from src.NLP_Text_Summary.pipeline.stage_01_data_ingestion import DataIngestionPipeline

logger.info("Welcome to my NLP project")


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.start_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e