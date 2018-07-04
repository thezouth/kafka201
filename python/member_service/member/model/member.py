import attr
import enum
import uuid

class NotificationChannel(enum.IntFlag):
    NONE  = 0x00
    EMAIL = 0x01
    LINE  = 0x02
    ALL   = 0xFF

@attr.s
class Member():
    name = attr.ib(type=str)
    privilege = attr.ib(type=str)

    email = attr.ib(type=str, default=None)
    line_account = attr.ib(type=str, default=None)

    id = attr.ib(type=str, default=attr.Factory(uuid.uuid4))
    notification_channel = attr.ib(type=NotificationChannel, default=NotificationChannel.NONE)
