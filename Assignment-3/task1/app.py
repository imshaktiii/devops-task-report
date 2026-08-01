from flask import Flask, jsonify,request,render_template,redirect 
import json
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# mongodb setup

client=pymongo.MongoClient(os.getenv("MONGO_URI"))
db=client.test
collection=db.formdata

# api 


@app.route('/api1')
def api():
    with open('data.json', 'r') as f:
        return jsonify(json.load(f))
#form
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        data = {
            'name': name,
            'email': email,
            'message': message
        }

        collection.insert_one(data)

        return redirect('/success')

    except Exception as e:
        return render_template('form.html', error=str(e))


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/test')
def test():
    return "test route works"



if __name__=='__main__':
    app.run(debug=True)
