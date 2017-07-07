from typing import Dict, Any

from grader.client import run_python

from .models import CodeRun


def run_code(*, code: str) -> CodeRun:
    result = run_python(code=code)

    run = CodeRun.objects.create(
        run_id=result['run_id'],
        run_status=result['run_status'],
        output=result['output']['test_output']
    )

    return run

