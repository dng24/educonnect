import login
import ratemyprof
import llm
import Algorithm

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['OPTIONS'])
def handle_options():
    resp = jsonify({"fooooooo": "bar"})
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Methods", "POST")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return resp

@app.route('/submit', methods=['POST'])
def submit():
    inputs = request.json
    print("Received inputs:", inputs)
    
    # step 1: get names of the professor teaching the given course
    class_code = inputs["class_code"]
    prof_names = login.get_professor_names(class_code)
    # step 2: get professor reviews from rate my professor
    rate_my_prof_info = ratemyprof.get_reviews(prof_names)
    
    # step 3: get professor ratings for each category based on rate my professor
    prof_ratings = []
    for prof_info in rate_my_prof_info:
        prof_ratings.append(llm.process_single_row(prof_info[0], prof_info[1]))

    # step 4: determine final compatibility score for each prof
    prof_compatibility = {}
    for rating in prof_ratings:
        compatibility = Algorithm.get_compatibility(rating, inputs["ratings"])
        prof_compatibility[compatibility[0]] = compatibility[1]
    
    print(rate_my_prof_info)
    resp = jsonify(prof_compatibility)
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Methods", "POST")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type")
    return resp

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
