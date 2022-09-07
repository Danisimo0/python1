import datetime
def get_datetime(formatstring: str) -> str:
    currenttime=datetime.datetime.now()
    match "":
        case "":
            load()
        case "":
            save()
        case :
            default()
    print(current_time)
    if formatstring=="07.09.2022 19:15":
        return current_time.strftime("%d.%m.%Y %H:%M")

    elif formatstring=="09.07.2022 19:15":
        return current_time.strftime("%m.%d.%Y %H:%M")

    elif formatstring=="09/07/2022 19:15":
        return current_time.strftime("%m/%d/%YT%H:%M")

    elif formatstring=="07-09-2022 ":
        return current_time.strftime("%d-%m-%Y")

    elif formatstring=="19:15":
        return current_time.strftime("%H:%M")


    return current_time.strftime("%m/%d/%YT%H:%M")
print(get_datetime("07.09.2022 19:15"))