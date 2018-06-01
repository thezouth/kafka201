from member.model.member import Member, NotificationChannel
import logging

admin = Member('admin-name', 'admin-priv',
        email='admin@webscal3r.club',
        notification_channel=NotificationChannel.EMAIL,
        id='admin-id')
members = {admin.id: admin}

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
