from housing.config.configuration import Configuration
from housing.component.data_ingestion import DataIngestion

conf=Configuration()
di=DataIngestion(conf.get_data_ingestion_config())
di.initiate_data_ingestion()