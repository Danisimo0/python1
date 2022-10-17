from processing_error_auth_file import AuthError



# first_int = int(input("Write first_int: "))
# second_int = int(input("Write second_int: "))
#
#
# def exception(func):
#     def excepted(first, second):
#         try:
#             result = func(first, second)
#         except ZeroDivisionError:
#             return "Can't divide by zero"
#         except OverflowError:
#             return "The number is big"
#         except ArithmeticError:
#             return "Eror"
#         return result
#
#     return excepted
#
#
# @exception
# def except_integer(first, second):
#     result = first / second
#     return result
#
#
# print(except_integer(first_int, second_int))


request_from_user1 = {
    "url": "localhost/home/",
    "method": "GET",
    "data": {"login attempt": 1},
    "timeout": 3000,
    "headers": {
        "Authorization": 'Admin',
    },
}

request_from_user2 = {
    "url": "localhost/",
    "method": "1",
    "data": {"login attempt": 1},
    "timeout": 3000,
    "headers": {},
}

request_from_user3 = {
    "url": "localhost/",
}
request_from_user4 = {

}

AuthError.auth_error(request_from_user3,check_request_keys=True, time_sleep=0.1)