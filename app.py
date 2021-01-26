from flask import Flask, request, redirect, render_template,flash
from flask_debugtoolbar import DebugToolbarExtension
app=Flask(__name__)

app.config['SECRET_KEY'] = 'FOO'
app.debug = True
EXPLAIN_TEMPLATE_LOADING = True

# @app.route('/old-site')
# def go_to_new_page():
#     return redirect('new-site.html')

# @app.route('/new-site')
# def to_to_new_site():
#     return render_template('new-site.html')

MOVIES = {'Star Wars', 'Life of Brian','Dances with Wolves','Firefly'}

@app.route('/movies')
def show_all_movies():
    """show list of all movies in fake db from list and display a one-line form to add more"""
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movie():
    title = request.form['title']
    #pretend DB code here
    if title in MOVIES:
        flash('Movie already exists', 'error')
    else:
        flash("MOVIE ADDED!", 'success')
        
    #can do the same route if wanted - but get 'confirm form re-submission' if they refresh and re-adds the same data
    #return render_template('movies.html', movies=MOVIES)
    #instead do a redirect that's just a GET request that will show the original with data from the list.  Avoids the refresh-repeat data problem!
    return redirect('/movies')

