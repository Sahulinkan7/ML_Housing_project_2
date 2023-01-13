from housing.config.configuration import Configuration
from housing.component.data_ingestion import DataIngestion

conf=Configuration()
print(conf.get_data_transformation_config())
di=DataIngestion(conf.get_data_ingestion_config())
di.initiate_data_ingestion()