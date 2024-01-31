def weekday_name(day_of_week):
    DAYS = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    if day_of_week < 1 or day_of_week > 7:
        return None
    return DAYS[day_of_week - 1]


weekday_name(1)
weekday_name(2)
weekday_name(3)
weekday_name(4)
weekday_name(5)
weekday_name(6)
weekday_name(7)
weekday_name(0)