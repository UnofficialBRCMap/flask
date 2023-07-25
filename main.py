import geopy
import geojson
from geopy.distance import geodesic
from geopy.distance import great_circle
from geojson import Polygon
from geojson import FeatureCollection
from flask import Flask, jsonify
import os

app = Flask(__name__)

centerCamp = [40.78052685763084, -119.21122602690583]

startingBearing = 360

def generateArtCoordinates(hour, minute, feet):
  bearing = (30 * hour) + (minute / 60)
  blockDict = {
    "coordinateToAppend": geopy.distance.distance(feet=feet).destination(centerCamp, bearing=(bearing))
  }
  centerCampCoordinates = [blockDict.get("coordinateToAppend")[0], blockDict.get("coordinateToAppend")[1]]
  print(centerCampCoordinates)
  return centerCampCoordinates


@app.route('/get-art-coordinates',methods = ['POST'])
def getCoordinates():
  hour = request.form['hour']
  minute = request.form['minute']
  feet = request.form['feet']
  response = jsonify(generateArtCoordinates(hour, minute, feet))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))