import logging

from sanic import Sanic, response
from sanic.exceptions import abort

import member

app = Sanic(__name__)


@app.route('/')
async def home(request):
    return response.json({'name': 'member service', 'version': '0.1', 'status': 'ok'})


@app.get('/member/<member_id>')
async def get_member(request, member_id):
    try:
        data = member.get(member_id)
    except member.MemberNotFoundException:
        abort(404)

    return response.json(data)


@app.post('/member/<member_id>/notify')
async def notify(request, member_id):
    try:
        message = request.json['message']
        member.notify(member_id, message)
    except member.MemberNotFoundException:
        abort(404)

    return response.json(
            {'status': 'success'},
            status=202)


@app.post('/member/<member_id>/promote')
async def promote(request, member_id):
    try:
        privilege = request.json['privilege']
        member.promote(member_id, privilege)
    except member.MemberNotFoundException:
        abort(404)

    return response.json({'status': 'success'})


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(port=8002)
