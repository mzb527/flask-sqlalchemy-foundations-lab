from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Earthquake

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)  # Ensures Flask-Migrate is properly set up

# API route to get an earthquake by ID
@app.route("/earthquakes/<int:id>")
def get_earthquake(id):
    earthquake = Earthquake.query.filter_by(id=id).first()
    if earthquake:
        return jsonify({
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        }), 200
    return jsonify({"message": f"Earthquake {id} not found."}), 404

# API route to get earthquakes above a given magnitude
@app.route("/earthquakes/magnitude/<float:magnitude>")
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return jsonify({
        "count": len(earthquakes),
        "quakes": [
            {"id": quake.id, "location": quake.location, "magnitude": quake.magnitude, "year": quake.year}
            for quake in earthquakes
        ]
    }), 200

# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)