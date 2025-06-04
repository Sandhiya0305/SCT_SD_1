from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

facts = [
    "Water freezes at 0°C and boils at 100°C.",
    "The highest recorded temperature on Earth is 56.7°C in Death Valley.",
    "Absolute zero is -273.15°C — the lowest possible temperature.",
    "A fever is usually over 38°C.",
    "Room temperature is around 20°C to 25°C.",
    "Liquid nitrogen boils at -196°C.",
    "The sun’s surface temperature is ~5500°C!",
    "Penguins can survive in temperatures below -60°C!",
    "Mercury is the only metal that is liquid at room temperature.",
    "At 37°C, the human body operates optimally."
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fact')
def get_fact():
    return jsonify({'fact': random.choice(facts)})

if __name__ == '__main__':
    app.run(debug=True)
