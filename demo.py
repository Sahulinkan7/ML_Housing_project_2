from housing.config.configuration import Configuration
from housing.component.data_ingestion import DataIngestion
from housing.exception import HousingException
from housing.component.data_transformation import DataTransformation
import sys
from housing.logger import logging
from housing.pipeline.pipeline import Pipeline

def main():
    try:
        # schema_file_path=r"E:\My new World\Ineuron\ML Projects\ML_Housing_project_2\config\schema.yaml"
        # file_path=r"E:\My new World\Ineuron\ML Projects\ML_Housing_project_2\housing\artifact\data_ingestion\2023-01-11-08-05-02\ingested_data\train\housing.csv"

        # df=DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)
        # print(df.shape)

        pipeline=Pipeline()
        pipeline.run_pipeline()
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()