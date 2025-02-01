from src.datascience import logger
from src.datascience.pipeline.step1_data_ingestion import DataIngestionTrainingPipeline
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