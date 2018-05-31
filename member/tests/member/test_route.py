import json

from server import app

def test_index():
    req, res = app.test_client.get('/')
    assert res.json.get('name') == 'member service'

def test_update():
    data = {'name': 'roong', 'privilege': 'silver'}
    req, res = app.test_client.post('/member/admin-id', data=json.dumps(data))
    assert res.status == 200
    assert res.json.get('name') == 'roong'

def test_user_not_found():
    req, res = app.test_client.get('/member/id-that-not-exists')
    assert res.status == 404

def test_user_found():
    req, res = app.test_client.get('/member/admin-id')
    assert res.status == 200
