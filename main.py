from src.datascience import logger
from src.datascience.pipeline.step1_data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.step2_data_validation import DATA_VALIDATION_TRAINING_PIPELINE
logger.info('weelcome to my logger')

STAGE_NAME='DATA_INGESTION_STAGE'

# if __name__=='__main__':
try:
          logger.info(f'<<<<<<<<<<<< stage {STAGE_NAME} started<<<<<<<<<')
          obj=DataIngestionTrainingPipeline()
          obj.initiate_data_ingestion()
          logger.info(f'>>>>>>>>>>stage {STAGE_NAME}  completed >>>>>>>>>>>>>')
except Exception as e:
           logger.exception(e)    
           raise e


STAGE_NAME='DATA_VALIDATION_STAGE'

# if __name__=='__main__':
try:
          logger.info(f'<<<<<<<<<<<< stage {STAGE_NAME} started<<<<<<<<<')
          obj=DATA_VALIDATION_TRAINING_PIPELINE()
          obj.initiate_datavalidation()
          logger.info(f'>>>>>>>>>>stage {STAGE_NAME}  completed >>>>>>>>>>>>>')
except Exception as e:
           logger.exception(e)    
           raise e