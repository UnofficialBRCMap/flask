import geopy
import geojson
from geopy.distance import geodesic
from geopy.distance import great_circle
from geojson import Polygon
from geojson import FeatureCollection
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

centerCamp = (40.786400, -119.203500)

startingBearing = 45

def generateArtCoordinates(hour, minute, feet):
  bearing = (30 * int(hour)) + (int(minute) / 60) + startingBearing
  if (bearing > 360): 
    bearing = bearing - 360
  blockDict = {
    "coordinateToAppend": geopy.distance.distance(feet=int(feet)).destination(centerCamp, bearing=(bearing))
  }
  centerCampCoordinates = [blockDict.get("coordinateToAppend")[0], blockDict.get("coordinateToAppend")[1]]
  print(centerCampCoordinates)
  return centerCampCoordinates


@app.route('/get-art-coordinates', methods = ['POST'])
def getCoordinates():
  hour = request.form['hour']
  minute = request.form['minute']
  feet = request.form['feet']
  response = jsonify(generateArtCoordinates(hour, minute, feet))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))