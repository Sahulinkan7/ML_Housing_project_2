from housing.exception import HousingException
from housing.logger import logging
import os,sys
import yaml
from housing.constant import *
from collections import namedtuple
import numpy as np

InitializedModelDetail=namedtuple("InitializedModelDetail",
["model_serial_number","model","param_grid_search","model_name"])

GridSearchedBestModel=namedtuple("GridSearchedBestModel",
["model_serial_number","model","best_model","best_parameters","best_score"])

BestModel=namedtuple("BestModel",
["model_serial_number","model","best_model","best_parameters","best_score"])

MetricInfoArtifact=namedtuple("MetricInfoArtifact",
["model_name","model_object","train_rmse","test_rmse","train_accuracy","test_accuracy","model_accuracy","index_number"])


def evaluate_regression_model(model_list:list,x_train:np.ndarray,y_train:np.ndarray,x_test:np.ndarray,y_test:np.ndarray,base_accuracy:float=0.6)->MetricInfoArtifact:
    """
    Description: 

    This function compares multiple regression model and return best model

    params:
    model_list: List of model
    x_train: training dataset input feature
    y_train: training dataset target feature
    x_test: testing dataset input feature
    y_test: testing dataset target feature

    return 
    it returns a named tuple MetricInfoArtifact

    MetricInfoArtifact = namedtuple("MetricInfo",
                                ["model_name", "model_object", "train_rmse", "test_rmse", "train_accuracy",
                                "test_accuracy", "model_accuracy", "index_number"])
    
    """
    try:
        pass
    except Exception as e:
        raise HousingException(e,sys) from e


class ModelFactory:
    def __init__(self,model_config_path:str=None):
        try:
            self.config:dict=ModelFactory.read_params(model_config_path)
            
            self.grid_search_cv_module: str=self.config[GRID_SEARCH_KEY][MODULE_KEY]
            self.grid_search_class_name: str=self.config[GRID_SEARCH_KEY][CLASS_KEY]
            self.grid_search_property_data: dict=dict(self.config[GRID_SEARCH_KEY][PARAM_KEY])
            self.model_initialization_config: dict=dict(self.config[MODEL_SELECTION_KEY])

            self.initialized_model_list=None
            self.grid_searched_best_model_list=None

        except Exception as e:
            raise HousingException(e,sys) from e

    @staticmethod
    def read_params(config_path:str)->dict:
        try:
            with open(config_path) as yaml_file:
                config:dict=yaml.safe_load(yaml_file)
            return config
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_best_model(self,x,y,base_accuracy=0.6) -> BestModel:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e