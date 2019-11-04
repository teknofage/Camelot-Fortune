from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')


@app.route('/fortune')
def fortune():
    """Renders the home Fortune page."""
    return render_template('fortune_results.html')


@app.route('/weather')
def weather():
    """Renders the Weather page."""
    return render_template('weather_results.html')


@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_preferred_drink = request.args.get('drink')
    # ... etc

    if users_preferred_drink == 'Beer':
        fortune is "You'll grow a beer belly and stop shaving as often!"
    elif users_preferred_drink == 'Wine':
        fortune is "You'll tell the best stories but your head will hut in the mornings!"
    elif users_preferred_drink == 'Mead':
        fortune is "You'll braid your hair and wield an axe with competence!"
    elif users_preferred_drink == 'Elderflower Cordial':
        fortune is "Your senses will never be dull, unlike your speeches!"
    elif users_preferred_drink == 'Love Potion Number 9':
        fortune is "You will fall madly in love with the wrong person, but it will be awesome while it lasts!"
    elif users_preferred_drink == 'Gorilla Punch':
        fortune is "You will fall over and need to be dragged to bed. Try not to wear your armour or you won't be able to get up!"
    else
        fortune is "You will feel unusually good about your quest for the Grail, even if you never find it!"
