from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')


@app.route('/fortune/new')
def fortune():
    """Renders the home Fortune page."""
    return render_template('fortune_form.html')


@app.route('/weather')
def weather():
    """Renders the Weather page."""
    return render_template('weather_results.html')

# @app.route('/fortunes', methods=['POST'])
# def fortunes_submit():
#     """Submit a new fortune."""
#     fortune = {
#         'title': request.form.get('title'),
#         'description': request.form.get('description'),
#         'videos': request.form.get('videos').split(),
#         'ratings': request.form.get('ratings')
#     }
#     playlist_id = playlists.insert_one(playlist).inserted_id
#     return redirect(url_for('playlists_show', playlist_id=playlist_id))

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_preferred_drink = request.args.get('drink')
    title = request.args.get('title')
    name = request.args.get('firstname')

    if users_preferred_drink == 'Beer':
        fortune = "You will grow a beer belly and stop shaving as often!"
    elif users_preferred_drink == 'Wine':
        fortune = "You will tell the best stories but your head will hurt in the mornings!"
    elif users_preferred_drink == 'Mead':
        fortune = "You will braid your hair and wield an axe with competence!"
    elif users_preferred_drink == 'Elderflower Cordial':
        fortune = "Your senses will never be dull, unlike your speeches!"
    elif users_preferred_drink == 'Love Potion Number 9':
        fortune = "You will fall madly in love with the wrong person, but it will be awesome while it lasts!"
    elif users_preferred_drink == 'Gorilla Punch':
        fortune = "You will fall over and need to be dragged to bed. Try not to wear your armour or you won't be able to get up!"
    else:
        fortune = "You will feel unusually good about your quest for the Grail, even if you never find it!"
    return render_template('fortune_results.html', fortune=fortune, title=title, name=name)