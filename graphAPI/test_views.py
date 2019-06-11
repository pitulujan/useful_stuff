import os
import tempfile
import pytest
import requests


def test_getID_Section():
    response = requests.get(
        'http://127.0.0.1:5000/graph_api/getID?sec=199A')

    assert response.status_code == 200, 'Check the valid parameter'


def test_getID_minusSection():
    response = requests.get(
        'http://127.0.0.1:5000/graph_api/getID?sec=-1')

    assert response.status_code == 403, 'Check invalid status'


def test_getRelationship_validNode():
    response = requests.get(
        'http://127.0.0.1:5000/graph_api/getRelationship/31694')

    assert response.status_code == 200, 'Chech valid status'


def test_getRelationship_invalidNode():
    response = requests.get(
        'http://127.0.0.1:5000/graph_api/getRelationship/-1')

    assert response.status_code == 403, 'Check invalid status'


def test_getNode_valid():
    response = requests.get(
        "http://127.0.0.1:5000/graph_api/getNode/31694")

    assert response.status_code == 200, 'Check valid status'


def test_getNode_invalid():
    response = requests.get("http://127.0.0.1:5000/graph_api/getNode/-1")

    assert response.status_code == 403, 'If this failed, check the invalid status'
