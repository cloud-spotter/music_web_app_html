import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

@app.route(f'/albums/<album_id>')
def get_single_album(album_id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    # albums = repository.all()
    # album = albums[0]
    album = repository.find(album_id)
    print(album)
    return render_template("albums/show.html", album=album)

## ---- Section 03 Exercise ---- ##
@app.route(f"/albums/<id>")
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template("albums/show.html", album=album)

@app.route(f"/albums/<id>")
def visit_album_show_page(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template("albums/show.html", album=album)



# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
