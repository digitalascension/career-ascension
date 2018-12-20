#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import omnidb

from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)
db = omnidb.OmniDB(host='192.168.33.40', user='root',passwd='rootpassword1234', database='OMNIDB')

@app.route('/')
def omni_index():
    models = []
    result = db.get_latest_models()
    for r in result:
        models.append(
            {
                'Name' : r[1],
                'CreatedBy' : r[2],
                'LastUpdated': r[3],
                'Tags' : r[4],
                'URL' : r[5]
             }
        )
    return render_template('index.html', models = models)

@app.route('/upload', methods=['GET'])
def create_model():
    return render_template('upload_model.html')

@app.route('/find', methods=['GET'])
def find_model():
    return render_template('find_model.html')

@app.route('/search/<value>', methods=['GET'])
def search_model(value):
    # Query the database and search for models like value.
    result = db.search_omni(value)
    print(result)
    return result

if __name__ == '__main__':
    app.run(debug=True)

