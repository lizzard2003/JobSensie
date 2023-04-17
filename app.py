# this app is made to as user questions about themselves to choose a careerpath
# we are using flask

#hello
from traitify import Traitify
secret_key= "API_KEY"
traitify= Traitify(secret_key)

decks= traitify.get_decks()

#set deck id
traitify.deck_id = decks[0].id

#create assessment
assessment= traitify.create_assessment()

#get assesment
assessment = traitify.get_assessment(assessment.id)

# Get an assessment's slides
slides = traitify.get_slides(assessment.id)

# Upate a slide
slide = slides[0]
slide.response = True
slide.time_taken = 200
slide = traitify.update_slide(assessment.id, slide)

# Bulk update slides
for slide in slides:
  slide.response = True
  slide.time_taken = 200
slides = traitify.update_slides(assessment.id, slides)

# Get an assessment's results (personality types)
personality_types = traitify.get_personality_types(assessment.id)

# Get an assessment's results (personality type traits)
personality_type = personality_types["personality_types"][0].personality_type

personality_traits = traitify.get_personality_type_traits(assessment.id, personality_type.id)

# Get an assessment's results (personality traits)
personality_traits = traitify.get_personality_traits(assessment.id)

# Get an assessment's results (personality traits raw, no dichotomy returned)
personality_traits_raw = traitify.get_personality_traits_raw(assessment.id)

# Get an assessment's career matches, only applicable to the `career-deck` deck
careers = traitify.career_matches(assessment.id)

# Get multiple types of results from an assessment
results = traitify.results(assessment.id, ["types", "traits", "blend"])

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "my_secret_key"

users = {} #dictionary to store user information (for this basic example)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            error = "Username already exists."
            return render_template('signup.html', error=error)
        users[username] = password
        session['username'] = username
        return redirect('/dashboard')
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users or users[username] != password:
            error = "Incorrect username or password."
            return render_template('login.html', error=error)
        session['username'] = username
        return redirect('/dashboard')
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

#sign up 
<!DOCTYPE html>
<html>
<head>
    <title>Sign up</title>
</head>
<body>
    <h1>Sign up</h1>
    {% if error %}
        <p>{{ error }}</p>
    {% endif %}
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username"><br>
        <label>Password:</label><br>
        <input type="password" name="password"><br>
        <input type="submit" value="Sign up">
    </form>
    <p>Already have an account? <a href="/login">Login</a></p>
</body>
</html>

login html 


<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    {% if error %}
        <p>{{ error }}</p>
    {% endif %}
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username"><br>
        <label>Password:</label><br>
        <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    <p>Don't have an account? <a href="/signup">Sign up</a></p>
</body>
</html>







dashboard.html 

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome to your dashboard, {{ username }}!</h1>
    <p>You have successfully logged in.</p>
    <p><a href="/logout">Logout</a></p>
</body>
</html>
