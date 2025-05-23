#!/usr/bin/env python3
from app import app
from models import db, Earthquake

with app.app_context():
    Earthquake.query.delete()

    earthquakes = [
        Earthquake(magnitude=9.5, location="Chile", year=1960),
        Earthquake(magnitude=9.2, location="Alaska", year=1964),
        Earthquake(magnitude=8.6, location="Alaska", year=1946),
        Earthquake(magnitude=8.5, location="Banda Sea", year=1934),
        Earthquake(magnitude=8.4, location="Chile", year=1922),
    ]

    db.session.add_all(earthquakes)
    db.session.commit()