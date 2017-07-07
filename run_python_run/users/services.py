import uuid
import time

from django.core.mail import send_mail

from django.db import transaction

from django.contrib.auth.models import User

from notifications.services import notify_slack


@transaction.atomic
def create_user(*,
                username: str,
                email: str,
                password: str) -> User:
    user = User(username=username, email=email, is_active=True)
    user.set_password(password)

    user.full_clean()
    user.save()

    return user


def send_confirmation_email(*, user: User) -> None:
    token = uuid.uuid4().hex

    send_mail(
        subject='Please confirm your registartion in Run-Python-Run!',
        message=token,
        from_email='noreply@runpythonrun.io',
        recipient_list=[user.email],
        fail_silently=False
    )


def send_welcome_email(*, user: User) -> None:
    send_mail(
        subject='Welcome to Run-Python-Run!',
        message='Have fun in the system',
        from_email='noreply@runpythonrun.io',
        recipient_list=[user.email],
        fail_silently=False
    )


def send_notifications(*, user: User) -> None:
    """
    TODO: Iterate over notifications app in more smart way
    """
    notify_slack(user=user)


def user_registration_flow(**kwargs) -> User:
    user = create_user(**kwargs)

    send_confirmation_email(user=user)

    time.sleep(2)

    send_notifications(user=user)
    send_welcome_email(user=user)

    return user
