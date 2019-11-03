from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')


@app.route('/fortune')
def fortune():
    """Renders the homFortune page."""
    return render_template('fortune_results.html')


@app.route('/weather')
def weather():
    """Renders the Weather page."""
    return render_template('weather_results.html')
