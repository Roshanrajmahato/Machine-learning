from logging import exception
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    logging.info("we are testing logging module")
    return "starting machine learning project"


if __name__=="_main_":
    app.run(debug=True)  



