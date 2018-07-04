from member.model.member import Member, NotificationChannel
import logging

members = {
    member.id: member
    for member in [
        Member('admin-name', 'admin-priv',
        email='admin@webscal3r.club',
        notification_channel=NotificationChannel.EMAIL,
        id='admin-id'),
        Member('YiM', 'silver', email='abc@xyz.com',
        NotificationChannel=NotificationChannel.EMAIL,
        id='1'),
        Member('Roong', 'silver', line_account='roongroong',
        NotificationChannel=NotificationChannel.LINE,
        id='2'),
    ]
}

logger = logging.getLogger(__name__)

def send_mail(mail_to, message):
    pass

def send_message(account, message):
    pass


def notify(member_id, message):
    member = get(member_id)
    channel_flag = member.notification_channel

    if channel_flag & NotificationChannel.EMAIL:
        send_mail(member.email, message)

    if channel_flag & NotificationChannel.LINE:
        send_message(member.line_account, message)


def promote(member_id, privilege):
    print('member', member_id, type(member_id))
    member = get(member_id)
    logger.info(f'Change member [{member_id}] privilege from "{member.privilege}" to "{privilege}"')
    member.privilege = privilege


def get(member_id):
    member = members.get(member_id)
    if member is None:
        raise MemberNotFoundException()

    return member


class MemberNotFoundException(Exception):
    pass
