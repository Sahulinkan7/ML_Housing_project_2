from housing.exception import HousingException
from housing.logger import logging
from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import Configuration
from housing.constant import CONFIG_DIR,get_current_time_stamp
import sys,os
from housing.entity.housing_predictor import HousingData,HousingPredictor

from flask import Flask,render_template,request

ROOT_DIR=os.getcwd()
SAVED_MODELS_DIR_NAME="saved_models"
MODEL_DIR=os.path.join(ROOT_DIR,SAVED_MODELS_DIR_NAME)

app=Flask(__name__)
HOUSING_DATA_KEY="housing_data"
MEDIAN_HOUSING_VALUE_KEY="median_house_value"

@app.route('/',methods=['GET','POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)


@app.route('/train',methods=['GET','POST'])
def train():
    message=""
    pipeline=Pipeline(config=Configuration(current_time_stamp=get_current_time_stamp()))
    if not Pipeline.experiment.running_status:
        message="Training Started"
        pipeline.start()
    else:
        message="Training is already in progress"
    context={
        "experiment":pipeline.get_experiment_status().to_html(classes='table table-striped col-12'),
        "message":message
    }
    return render_template('train.html',context=context)

@app.route('/experiment_history',methods=['GET','POST'])
def view_history():
    pipeline=Pipeline(config=Configuration(current_time_stamp=get_current_time_stamp()))
    experiment_df=pipeline.get_experiment_status()
    context={
        "experiment":experiment_df.to_html(classes='table table-striped col-12')
    }
    return render_template('experiment_history.html',context=context)

@app.route('/predict',methods=['GET','POST'])
def predict():
    context={
        HOUSING_DATA_KEY:None,
        MEDIAN_HOUSING_VALUE_KEY:None
    }

    if request.method=='POST':
        longitude=float(request.form['longitude'])
        latitude=float(request.form['latitude'])
        housing_median_age=float(request.form['housing_median_age'])
        total_rooms=float(request.form['total_rooms'])
        total_bedrooms=float(request.form['total_bedrooms'])
        population=float(request.form['population'])
        households=float(request.form['households'])
        median_income=float(request.form['median_income'])
        ocean_proximity=request.form['ocean_proximity']

        housing_data=HousingData(longitude=longitude,
                                 latitude=latitude,
                                 housing_median_age=housing_median_age,
                                 total_rooms=total_rooms,
                                 total_bedrooms=total_bedrooms,
                                 population=population,
                                 households=households,
                                 median_income=median_income,
                                 ocean_proximity=ocean_proximity)

        housing_df=housing_data.get_housing_input_data_frame()
        housing_predictor=HousingPredictor(model_dir=MODEL_DIR)
        median_housing_value=housing_predictor.predict(x=housing_df)
        context={
            HOUSING_DATA_KEY:housing_data.get_housing_data_as_dict(),
            MEDIAN_HOUSING_VALUE_KEY: median_housing_value
        }

        return render_template('predict.html',context=context)
    return render_template('predict.html',context=context)


if __name__=="__main__":
    app.run(debug=True)