import cgi
import login
import ratemyprof
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    inputs = request.json
    print("Received inputs:", inputs)
    # step 1: get names of the professor teaching the given course
    class_code = inputs["class_code"]
    prof_names = login.get_professor_names(class_code)
    # step 2: get professor reviews from rate my professor
    rate_my_prof_info = ratemyprof.get_reviews(prof_names)
    
    print(rate_my_prof_info)
    return ""

if __name__ == "__main__":
    app.run(debug=True)
