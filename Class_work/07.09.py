import datetime


def get_datetime(formatstring: str) -> str:
    current_time = datetime.datetime.now()
    match formatstring:
        case "07.09.2022 19:15":
            return current_time.strftime("%d.%m.%Y %H:%M")
        case "09.07.2022 19:15":
            return current_time.strftime("%m.%d.%Y %H:%M")
        case "09/07/2022 19:15":
            return current_time.strftime("%m/%d/%YT%H:%M")
        case "07-09-2022":
            return current_time.strftime("%d-%m-%Y")
        case "19:15":
            return current_time.strftime("%H:%M")
        case _:
            return current_time.strftime("%m/%d/%YT%H:%M")
    print(current_time)
    if formatstring == "07.09.2022 19:15":
        return current_time.strftime("%d.%m.%Y %H:%M")

    elif formatstring == "09.07.2022 19:15":
        return current_time.strftime("%m.%d.%Y %H:%M")

    elif formatstring == "09/07/2022 19:15":
        return current_time.strftime("%m/%d/%YT%H:%M")

    elif formatstring == "07-09-2022 ":
        return current_time.strftime("%d-%m-%Y")

    elif formatstring == "19:15":
        return current_time.strftime("%H:%M")

    return current_time.strftime("%m/%d/%YT%H:%M")


# print(get_datetime("07.09.2022 19:15"))

class CustomTime:
    def init(self, date_time=None):
        if date_time is None:

            self.current_time = datetime.datetime.now()
        else:
            self.current_time = date_time

    def get_time(self) -> str:
        return self.current_time.strftime("%H:%M")

    def get_sql_datetime(self) -> str:
        return self.current_time.strftime("%m/%d/%YT%H:%M")

    def get_europian_datetime(self) -> str:
        return self.current_time.strftime("%d.%m.%Y %H:%M")
    @staticmethod
    def get_static_datetime() -> str:
        return datetime.datetime.now().strftime("%d.%m.%Y %H:%M")


time1 = CustomTime()
print(time1.current_time)
print(time1.get_time())
time2 = CustomTime(date_time=datetime.datetime.now() - datetime.timedelta(minutes = 30))
print(time2.get_time())