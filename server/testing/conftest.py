#!/usr/bin/env python3

import pytest
from app import app, db
from models import Plant

@pytest.fixture(scope="session", autouse=True)
def seed_database():
    with app.app_context():
        db.create_all()
        Plant.query.delete()
        aloe = Plant(id=1, name="Aloe", image="./images/aloe.jpg", price=11.50)
        zz_plant = Plant(id=2, name="ZZ Plant", image="./images/zz-plant.jpg", price=25.98)
        db.session.add_all([aloe, zz_plant])
        db.session.commit()

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
