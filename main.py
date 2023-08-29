from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.logging import logger


stage_name = "Data ingestion stage"
try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {stage_name} complete <<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e