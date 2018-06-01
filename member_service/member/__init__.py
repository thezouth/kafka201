from member.model.member import Member
import logging

admin = Member('admin-id', 'admin-name', 'admin-priv')
members = {admin.id: admin}

logger = logging.getLogger(__name__)


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