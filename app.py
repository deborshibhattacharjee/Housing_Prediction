from operator import index
from flask import Flask, request, render_template
from model import predict_housing_price
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cc69aeb9e22f352180710480ab0b0c78953d15d16ead0af369141356108fcbb9'

@app.route('/',methods=["GET","POST"])
def home():
    message = "Welcome to my first flask based web application ... !!!"
    return render_template("home.html", message = message)

@app.route('/getResponseModel',methods=["GET","POST"])
def getResponseModel():
    d = request.form.to_dict()

    model = joblib.load("model_files\my_model.pkl")
        
    
    y_pred = predict_housing_price(d, model)
    return y_pred


if __name__ == '__main__':
    app.run(debug=True)