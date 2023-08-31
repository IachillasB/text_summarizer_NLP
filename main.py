from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
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


stage_name = "Data validation stage"
try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {stage_name} complete <<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Data transformation stage"
try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>> stage {stage_name} complete <<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Data model trainer stage"
try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    data_transformation = ModelTrainerTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>> stage {stage_name} complete <<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e
