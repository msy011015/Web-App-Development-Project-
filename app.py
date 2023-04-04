from flask import Flask, render_template, request
from mbta_helper import get_lat_long, get_nearest_station, find_stop_near

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/MBTA/', methods = ["GET", "POST"])
def MBTA():
    if request.method == "POST":
        place_name = str(request.form["place"])
        result = find_stop_near(place_name)
        if result:
            station_name, wheelchair_accessible = result
            return render_template("result.html", station_name = station_name, wheelchair_accessible = wheelchair_accessible )
        else:
            return render_template("form.html", error = True)
    return render_template("form.html", error = None)
 
 
if __name__ == '__main__':
    app.run(debug=True)
 