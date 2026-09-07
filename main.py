from src.NLP_Text_Summary.logging import logger
from src.NLP_Text_Summary.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.NLP_Text_Summary.pipeline.stage_02_date_validation import DataValidationPipeline



logger.info("Welcome to my NLP project")


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e