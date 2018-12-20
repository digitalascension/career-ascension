#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import omnidb

from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)
db = omnidb.OmniDB(host='192.168.33.40', user='root',passwd='rootpassword1234', database='OMNIDB')

@app.route('/')
def ca_index():
    postings = []
    result = db.get_latest_models()
    for r in result:
        postings.append(
            {
                'Company' : r[1],
                'Title' : r[2],
             }
        )
    postings.append(
        {
            'Company': 'Test1',
            'Title': 'Site Reliability Engineer',
        }
    )
    return render_template('index.html', postings = postings)

@app.route('/category/<category>', methods=['GET'])
def get_category(category):
    return render_template('job_category.html')

@app.route('/post', methods=['GET'])
def find_model():
    return render_template('post_job.html')

@app.route('/search/<value>', methods=['GET'])
def search_model(value):
    # Query the database and search for models like value.
    result = db.search_omni(value)
    print(result)
    return result

if __name__ == '__main__':
    app.run(debug=True)

