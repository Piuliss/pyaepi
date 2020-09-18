"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, ConnSpeedTest

api = Blueprint('api', __name__)


@api.route('/speed_tests/<int:id>/', methods=['GET'])
def speed_test(id):
    speed_test = ConnSpeedTest.query.get(id)
    return jsonify({'speed_test': speed_test.to_dict()})


@api.route('/speed_tests/', methods=('GET', 'POST'))
def speed_tests():
    if request.method == 'GET':
        data = {'speed_tests': [s.to_dict() for s in ConnSpeedTest.query.all()]}
        return jsonify(data)
    elif request.method == 'POST':
        data = request.get_json()
        speed_test = ConnSpeedTest(download=data['download'],
                                   upload=data['upload'],
                                   ping=data['ping'])
        db.session.add(speed_test)
        db.session.commit()
        return jsonify(speed_test.to_dict()), 201
