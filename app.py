from flask import Flask,request,render_template

from src.mlProject.pipeline import prediction_pipeline
from src.mlProject.pipeline.prediction_pipeline import CustomData

app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("home.html")
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        
        final_data=data.get_data_as_dataframe()

        predict_pipeline=prediction_pipeline()

        pred=predict_pipeline.predict(final_data)

        result=round(pred[0],2)

        return render_template("result.html",final_result=result)



if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)