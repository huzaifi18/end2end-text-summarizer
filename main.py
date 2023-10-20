from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_intestion = DataIngestionTrainingPipeline()
    data_intestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX==========X")
    
except Exception as e:
    logger.exception(e)
    raise e