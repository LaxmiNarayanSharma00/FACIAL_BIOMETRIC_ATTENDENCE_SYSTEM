from src.datascience.constants import *
from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience.utils.common import read_yml,create_directories
class ConfigManager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH,SCHEMA_FILE_PATH=SCHEMA_FILE_PATH):
        self.config=read_yml(config_file_path)
        self.params=read_yml(params_file_path)
        self.schema=read_yml(SCHEMA_FILE_PATH)

        create_directories([self.config.artifacts_roots])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
                root_dir=config.root_dir,
                source_url=config.source_url,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            
        )

        return data_ingestion_config


        