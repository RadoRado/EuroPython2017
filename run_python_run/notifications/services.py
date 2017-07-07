import requests

from django.conf import settings

from django.contrib.auth.models import User


def notify_slack(*, user: User) -> None:
    slack_hook = settings.SLACK_WEB_HOOK

    if bool(slack_hook) is False:
        print('No slack hook found. Please set SLACK_WEB_HOOK')
        return

    channel = settings.SLACK_CHANNEL or '#general'

    data = {
        'channel': channel,
        'username': 'Run-Python-Run Bot!',
        'text': 'New user registered -> {email}'.format(email=user.email),
        'icon_emoji': ':ok_hand:'
    }

    requests.post(slack_hook, json=data)
