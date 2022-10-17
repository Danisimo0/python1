import time
from pprint import pprint
import sys


animation = ["■□□□□□□□□□", "■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□",
             "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■", "Processing completed \n"]
request_keys_default = ["url", "method", "data", "timeout", "headers"]
methods_default = ["GET", "POST", "PUT", "DELETE", "AUTH", "HEAD", "PATCH"]


def processing_error_auth(func):
    def excepted(request_data, time_sleep=0.5, check_request_keys=True, check_methods=True,
                 request_keys=request_keys_default, methods=methods_default):

        print("Start")
        for i in range(len(animation)):
            time.sleep(time_sleep)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        if len(request_data) == 0:
            print("Eror")
            time.sleep(.2)
            raise KeyError('Empty')

        if check_request_keys:
            if len(request_data) < 5:
                print('Missing elements with a key:')
                for i in request_keys:
                    if request_data.get(i, None):
                        pass
                    else:
                        print(i)
        else:
            print('Key verification disabled')

        if check_methods:
            try:
                if request_data["method"] not in methods:
                    request_data_except = request_data["method"]
                    raise NonExistentMethod(error=request_data_except)
            except KeyError:
                pass
        else:
            print("Method validation disabled")

        result = func(request_data)

        return result

    return excepted


class AuthError:
    @processing_error_auth
    def auth_error(self):
        print("Your dictionary: ")
        pprint(self)


class NonExistentMethod(Exception):

    def __init__(self, error, ):
        self.message = f"This method '{error}' doesn't exist"

        super().__init__(self.message)