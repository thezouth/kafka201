import json

from rest_server import app

def test_index():
    _, res = app.test_client.get('/')
    assert res.json.get('name') == 'member service'

def test_promote():
    data = {'privilege': 'silver'}
    _, res = app.test_client.post('/member/admin-id/promote', data=json.dumps(data))
    assert res.status == 200
    assert res.json.get('status') == 'success'

def test_user_not_found():
    _, res = app.test_client.get('/member/id-that-not-exists')
    assert res.status == 404

def test_user_found():
    _, res = app.test_client.get('/member/admin-id')
    assert res.status == 200
