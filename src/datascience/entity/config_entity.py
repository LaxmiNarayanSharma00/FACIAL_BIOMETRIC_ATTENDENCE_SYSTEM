from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class Datavalidationconfig:
    root_dir:Path
    unzip_data_dir:Path
    STATUS_FILE:str
    all_schema:dict

@dataclass
class Datatransformation_config:
    root_dir: Path
    data_path: Path    