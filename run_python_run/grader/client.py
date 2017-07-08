from typing import Dict

import time

import base64

import requests

from django.conf import settings


def poll_for_result(*, check_url: str) -> Dict[str, str]:
    response = requests.get(check_url, timeout=2)

    while response.status_code == 204:
        run_status = response.headers['X-Run-Status']
        response = requests.get(check_url, timeout=2)

        time.sleep(1)

    return response.json()


def run_python(*, code: str) -> Dict[str, str]:
    code = base64.b64encode(code.encode('utf-8')).decode('ascii')
    test = base64.b64encode('import solution'.encode('utf-8')).decode('ascii')

    payload = {
        'test_type': 'unittest',
        'language': 'python',
        'solution': code,
        'test': test,
        'extra_options': {
            'lint': False
        }
    }

    response = requests.post(settings.GRADER_SUBMIT_URL, json=payload, timeout=2)

    if response.status_code not in [200, 202]:
        raise ValueError(response.text)

    check_url = response.headers['Location']
    run_id = response.json()['run_id']

    result = poll_for_result(check_url=check_url)

    return result
