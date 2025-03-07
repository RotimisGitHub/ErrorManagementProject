import datetime
import inspect
import json
import os.path
from functools import wraps
from pprint import pprint


def capture_error(func):
    @wraps(func)
    def wrapper():
        function_name = func.__name__

        try:

            print(f'Executing {function_name}')
            func()
            print(f"Successfully Executed {function_name}")
            answer = input(f"Successfully Executed {function_name} we've noticed there was an error prior. Was the error resolved? (Y/n)")
            if answer == 'Y':
                # Proceed to correct database. input this into solutions table and mark error as solved
            else:
                # Increment repeat field in database for recurring error. Then Give advice on how to solve error



        except Exception as e:
            traceback_sequence = inspect.trace()
            frame = [i for i in traceback_sequence if i.function == function_name][0]

            error_documents = {
                'current_time': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                'current_document': os.path.basename(__file__),
                'function name': frame.function,
                'specific line': frame.lineno,
                'function with error': inspect.getsource(func),
                'error': type(e).__name__,
                'error message': str(e).split(type(e).__name__)[0],
                'module': e.__class__.__module__,
                'code': frame.code_context[0].strip() if frame.code_context else "Unknown"
                                                                                 'times failed'
            }

            pprint(error_documents)

    return wrapper


@capture_error
def json_failure():
    invalid_json = "{'key': 'value'}"
    return json.loads(invalid_json)


json_failure()
