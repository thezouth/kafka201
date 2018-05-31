from attr import attrs, attrib

@attrs
class Member():
    id = attrib()
    name = attrib()
    privilege = attrib()
