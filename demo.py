from housing.config import configuration

conf=configuration.Configuration()
x=conf.get_training_pipeline_config()
print(x)
y=conf.get_data_ingestion_config()
print(y)
