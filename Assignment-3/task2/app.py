from flask import Flask,request,render_template
from dotenv import load_dotenv

import os
import pymongo



load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')
client=pymongo.MongoClient(MONGO_URI)
db=client.test
collection=db['task2_data']

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()  

    collection.insert_one(form_data)
    return "Data submitted successfully!"


@app.route('/view')
def view():
     data=collection.find()
     data=list(data)
     for item in data:
         print(item)
         del item['_id']

     data={
         'data':data
     
     }
     return data

if __name__ == '__main__':

    app.run(debug=True)

     
