from flask import (Flask,
                   render_template,
                   abort)

import data

app = Flask(__name__)


@app.route('/')
def index():
    output = render_template("index.html",
                             tours=data.tours,
                             all_departures=data.departures)
    return output


@app.route('/from/<direction>')
def departure(direction):
    tours_from_direction = {}
    for tour_id in data.tours:
        if data.tours[tour_id]["departure"] == direction:
            tours_from_direction[tour_id] = data.tours[tour_id]
    if not tours_from_direction:
        abort(404)

    min_price = min([tours_from_direction[tour_id]['price'] for tour_id in tours_from_direction])
    max_price = max([tours_from_direction[tour_id]['price'] for tour_id in tours_from_direction])
    min_nights = min([tours_from_direction[tour_id]['nights'] for tour_id in tours_from_direction])
    max_nights = max([tours_from_direction[tour_id]['nights'] for tour_id in tours_from_direction])

    output = render_template("direction.html",
                             tours=tours_from_direction,
                             departure=data.departures[direction],
                             all_departures=data.departures,
                             min_price=min_price,
                             max_price=max_price,
                             min_nights=min_nights,
                             max_nights=max_nights)
    return output


@app.route('/tours/<tour_id>')
def tour(tour_id):
    tour_id = int(tour_id)
    if tour_id not in data.tours:
        abort(404)
    tour_data = data.tours[tour_id]
    output = render_template("tour.html",
                             tour_data=tour_data,
                             all_departures=data.departures)
    return output


if __name__ == '__main__':
    app.run()
