from flask import Flask, request, render_template, session, redirect

app = Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/', methods=['POST','GET'])
# def submit_form():
#     if request.method == "POST":
#         budget = request.form['budget']
#         event_theme = request.form['Event_Theme']
#         num_people = request.form['num_people']
#         cuisine = request.form['Cuisine']
#         genre = request.form['Genre']
#         dress_type = request.form['Dress_Type']
#         tier = request.form['Tier']

#     print(budget, event_theme, num_people, cuisine, genre,dress_type, tier)
#     return render_template("Analyzing_Page/index.html")

    # return 'Form submitted successfully!'
@app.route('/', methods=['POST','GET'])
def submit_form():
    if request.method == "POST":
        try:
            budget = request.form['budget']
        except KeyError:
            budget = None
        
        try:
            event_theme = request.form['Event_Theme']
        except KeyError:
            event_theme = None
        
        try:
            num_people = request.form['num_people']
        except KeyError:
            num_people = None
        
        try:
            cuisine = request.form['Cuisine']
        except KeyError:
            cuisine = None
        
        try:
            genre = request.form['Genre']
        except KeyError:
            genre = None
        
        try:
            dress_type = request.form['Dress_Type']
        except KeyError:
            dress_type = None
        
        try:
            tier = request.form['Tier']
        except KeyError:
            tier = None

        session['budget'] = budget
        session['event_theme'] = event_theme
        session['num_people'] = num_people
        session['cuisine'] = cuisine
        session['genre'] = genre
        session['dress_type'] = dress_type
        session['tier'] = tier

        # Redirect to another Python file
        return redirect('src/BackEndWeddingPlanner.py')
        
    return render_template("Analyzing_Page/index.html")

def get_budget():
    return session.get('budget')

def get_event_theme():
    return session.get('event_theme')

def get_num_people():
    return session.get('num_people')

def get_cuisine():
    return session.get('cuisine')

def get_genre():
    return session.get('genre')

def get_dress_type():
    return session.get('dress_type')

def get_tier():
    return session.get('tier')


if __name__ == '__main__':
    app.run(debug=True)
