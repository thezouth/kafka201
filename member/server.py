from sanic import Sanic, response
from sanic.exceptions import abort

from member.model.member import Member

app = Sanic(__name__)

admin = Member('admin-id', 'admin-name', 'admin-priv')
members = {admin.id: admin}

@app.route('/')
async def home(request):
    return response.json({'name': 'member service', 'version': '0.1', 'status': 'ok'})


@app.route('/member/<member_id>', methods=['PUT', 'POST'])
async def put_member(request, member_id):
    member = members.get(member_id)
    if members.get(member_id) is None:
        abort(404)

    data = request.json
    member.name = data['name'] if data.get('name') is not None else member.name
    member.privilege = data['privilege'] if data.get('privilege') is not None else member.privilege

    return response.json(members[member_id])


@app.get('/member/<member_id>')
async def get_member(request, member_id):
    member = members.get(member_id)
    if member is None:
        abort(404)
    return response.json(member)

if __name__ == '__main__':
    app.run()
