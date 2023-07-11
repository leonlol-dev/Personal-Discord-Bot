from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import math


def TimeDifference(timeNow, timeBus):
    # This function finds out how many minutes til next bus
    now = datetime.strptime(timeNow, "%H:%M")
    bus = datetime.strptime(timeBus, "%H:%M")

    delta = bus - now

    # difference
    sec = delta.total_seconds()
    ans = sec / 60

    return math.floor(ans)


def TimeAdd(timeNow, timeBusMinutes):
    # This functions finds out what time based on how many minutes til next bus
    now = datetime.strptime(timeNow, "%H:%M")
    mins = float(timeBusMinutes)

    ans = now + timedelta(minutes=mins)

    return ans.strftime("%H:%M")


def getCurrentTime():
    # TIME
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


def busWebScrape():
    # TIME
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)

    # THAMES VALLEY BUS VANDYKE NORTH BOUND
    html_text = requests.get("https://www.thamesvalleybuses.com/stops/0380E283I250")
    try:
        soup = BeautifulSoup(html_text.content, "lxml")
        thamesValleyBus = soup.find("li", class_="departure-board__item")
        thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

        stringInfo = thamesValleyNextBus.text.split()

        vandykeNorthService = stringInfo[2]
        vandykeNortharrival = 0
        vandykeNorthtime = 0

        # Check if the website's bus infomation is showing minutes or time

        for i in range(8, len(stringInfo)):
            if stringInfo[i] == "mins.":
                vandykeNortharrival = stringInfo[i - 1]
                vandykeNorthtime = TimeAdd(current_time, vandykeNortharrival)
                break

            if stringInfo[i] == "min.":
                vandykeNortharrival = stringInfo[i - 1]
                time = TimeAdd(current_time, vandykeNortharrival)
                break

            if stringInfo[i] == "Due.":
                vandykeNortharrival = 0
                time = current_time
                break

        if vandykeNortharrival == 0 and vandykeNorthtime == 0:
            vandykeNorthtime = stringInfo[11]
            vandykeNorthtime = vandykeNorthtime[:-1]
            vandykeNortharrival = TimeDifference(current_time, vandykeNorthtime)

        print(
            f"""
            (Vandyke North Bound Bus Stop) Next Bus Information:
            Service: {vandykeNorthService}
            Time: {vandykeNorthtime}
            Arrival: {vandykeNortharrival} Minutes
            """
        )

    except:
        pass

    # VANDYKE SOUTH BOUND READING LION 4 BUS
    html_text = requests.get("https://www.reading-buses.co.uk/stops/0380E293I261")

    try:
        soup = BeautifulSoup(html_text.content, "lxml")
        thamesValleyBus = soup.find("li", class_="departure-board__item")
        thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

        stringInfo = thamesValleyNextBus.text.split()
        vandykeSouthService = 4

        vandykeSoutharrival = 0
        vandykeSouthtime = 0

        # Check if the website's bus infomation is showing minutes or time
        for i in range(8, len(stringInfo)):
            if stringInfo[i] == "mins.":
                vandykeSoutharrival = stringInfo[i - 1]
                vandykeSouthtime = TimeAdd(current_time, vandykeSoutharrival)
                break

            if stringInfo[i] == "min.":
                vandykeSoutharrival = stringInfo[i - 1]
                time = TimeAdd(current_time, vandykeSoutharrival)
                break

            if stringInfo[i] == "Due.":
                vandykeSoutharrival = 0
                time = current_time
                break

        if vandykeSoutharrival == 0 and vandykeSouthtime == 0:
            vandykeSouthtime = stringInfo[10]
            vandykeSouthtime = vandykeSouthtime[:-1]
            vandykeSoutharrival = TimeDifference(current_time, vandykeSouthtime)

        print(
            f"""
            (Vandyke South Bound Bus Stop) Next Bus Information:
            Service: {vandykeSouthService}
            Time: {vandykeSouthtime}
            Arrival: {vandykeSoutharrival} Minutes
            """
        )

    except:
        pass

    # THAMES VALLEY BUS ULLSWATER NORTH BOUND
    html_text = requests.get("https://www.thamesvalleybuses.com/stops/0380E413J975")

    try:
        soup = BeautifulSoup(html_text.content, "lxml")
        thamesValleyBus = soup.find("li", class_="departure-board__item")
        thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

        stringInfo = thamesValleyNextBus.text.split()
        ullswaterNorthservice = stringInfo[2]

        ullswaterNortharrival = 0
        ullswaterNorthtime = 0

        # Check if the website's bus infomation is showing minutes or time

        for i in range(8, len(stringInfo)):
            if stringInfo[i] == "mins.":
                ullswaterNortharrival = stringInfo[i - 1]
                ullswaterNorthtime = TimeAdd(current_time, ullswaterNortharrival)
                break

            if stringInfo[i] == "min.":
                ullswaterNortharrival = stringInfo[i - 1]
                time = TimeAdd(current_time, ullswaterNortharrival)
                break

            if stringInfo[i] == "Due.":
                ullswaterNortharrival = 0
                time = current_time
                break

            # if last element in list doesn't contain the words 'mins.', Will assume it's a time not a duration
            # stringInfo[11] is hard coded, idc LOL. But every 11th element should include the time.
            # else:
            #     ullswaterNorthtime = stringInfo[11]
            #     ullswaterNorthtime = ullswaterNorthtime[:-1]
            #     ullswaterNortharrival = TimeDifference(current_time, ullswaterNorthtime)

        if ullswaterNortharrival == 0 and ullswaterNorthtime == 0:
            ullswaterNorthtime = stringInfo[11]
            ullswaterNorthtime = ullswaterNorthtime[:-1]
            ullswaterNortharrival = TimeDifference(current_time, ullswaterNorthtime)

        print(
            f"""
            (Ullswater North Bound Bus Stop) Next Bus Information:
            Service: {ullswaterNorthservice}
            Time: {ullswaterNorthtime}
            Arrival: {ullswaterNortharrival} Minutes
            """
        )

    except:
        pass

    numbersList = [
        vandykeNorthService,
        vandykeNorthtime,
        vandykeNortharrival,
        vandykeSouthService,
        vandykeSouthtime,
        vandykeSoutharrival,
        ullswaterNorthservice,
        ullswaterNorthtime,
        ullswaterNortharrival,
    ]

    return numbersList


def busHomeScrape():
    # TIME
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)

    # THAMES VALLEY BUS BRACKNELL BUS STATION BAY 9
    html_text = requests.get("https://www.thamesvalleybuses.com/stops/0380F992G030")

    soup = BeautifulSoup(html_text.content, "lxml")
    thamesValleyBus = soup.find("li", class_="departure-board__item")
    thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

    stringInfo = thamesValleyNextBus.text.split()
    bayNineservice = stringInfo[2]

    bayNinearrival = 0
    bayNinetime = 0

    # Check if the website's bus infomation is showing minutes or time

    for i in range(8, (len(stringInfo))):
        if stringInfo[i] == "mins.":
            bayNinearrival = stringInfo[i - 1]
            bayNinetime = TimeAdd(current_time, bayNinearrival)
            break

        if stringInfo[i] == "min.":
            bayNinearrival = stringInfo[i - 1]
            bayNinetime = TimeAdd(current_time, bayNinearrival)
            break

        if stringInfo[i] == "Due.":
            bayNinearrival = 0
            bayNinetime = current_time
            break

    if bayNinearrival == 0 and bayNinetime == 0:
        bayNinetime = stringInfo[11]
        bayNinetime = bayNinetime[:-1]
        bayNinearrival = TimeDifference(current_time, bayNinetime)

    print(
        f"""
        (Bracknell Bus Station Bay 9 Bus Stop) Next Bus Information:
        Service: {bayNineservice}
        Time: {bayNinetime}
        Arrival: {bayNinearrival} Minutes
        """
    )

    # THAMES VALLEY BUS BRACKNELL BUS STATION BAY 7
    html_text = requests.get("https://www.thamesvalleybuses.com/stops/0380F992G059")

    soup = BeautifulSoup(html_text.content, "lxml")
    thamesValleyBus = soup.find("li", class_="departure-board__item")
    thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

    stringInfo = thamesValleyNextBus.text.split()
    baySevenservice = stringInfo[2]

    baySevenarrival = 0
    baySeventime = 0

    # Check if the website's bus infomation is showing minutes or time

    for i in range(8, (len(stringInfo))):
        if stringInfo[i] == "mins.":
            baySevenarrival = stringInfo[i - 1]
            baySeventime = TimeAdd(current_time, baySevenarrival)
            break

        if stringInfo[i] == "min.":
            baySevenarrival = stringInfo[i - 1]
            baySeventime = TimeAdd(current_time, baySevenarrival)
            break

        if stringInfo[i] == "Due.":
            baySevenarrival = 0
            baySeventime = current_time
            break

    if baySevenarrival == 0 and baySeventime == 0:
        baySeventime = stringInfo[11]
        baySeventime = baySeventime[:-1]
        baySevenarrival = TimeDifference(current_time, baySeventime)

    print(
        f"""
        (Bracknell Bus Station Bay 9 Bus Stop) Next Bus Information:
        Service: {baySevenservice}
        Time: {baySeventime}
        Arrival: {baySevenarrival} Minutes
        """
    )

    # LION BUS BRACKNELL BUS STATION BAY 5
    html_text = requests.get("https://www.reading-buses.co.uk/stops/0380F981G045")

    soup = BeautifulSoup(html_text.content, "lxml")
    thamesValleyBus = soup.find("li", class_="departure-board__item")
    thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

    stringInfo = thamesValleyNextBus.text.split()
    print(thamesValleyNextBus.text)
    bayFiveservice = 4

    bayFivearrival = 0
    bayFivetime = 0

    # Check if the website's bus infomation is showing minutes or time

    for i in range(8, (len(stringInfo))):
        if stringInfo[i] == "mins.":
            bayFivearrival = stringInfo[i - 1]
            bayFivetime = TimeAdd(current_time, bayFivearrival)
            break

        if stringInfo[i] == "min.":
            bayFivearrival = stringInfo[i - 1]
            bayFivetime = TimeAdd(current_time, bayFivearrival)
            break

        if stringInfo[i] == "Due.":
            bayFivearrival = 0
            bayFivetime = current_time
            break

    if bayFivearrival == 0 and bayFivetime == 0:
        bayFivetime = stringInfo[10]
        bayFivetime = bayFivetime[:-1]
        bayFivearrival = TimeDifference(current_time, bayFivetime)

    print(
        f"""
        (Bracknell Bus Station Bay 9 Bus Stop) Next Bus Information:
        Service: {bayFiveservice}
        Time: {bayFivetime}
        Arrival: {bayFivearrival} Minutes
        """
    )

    numbersList = [
        bayNineservice,
        bayNinetime,
        bayNinearrival,
        baySevenservice,
        baySeventime,
        baySevenarrival,
        bayFiveservice,
        bayFivetime,
        bayFivearrival,
    ]

    return numbersList


def vandykeNorthBoundScrape():
    # TIME
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)

    # THAMES VALLEY BUS VANDYKE NORTH BOUND
    html_text = requests.get("https://www.thamesvalleybuses.com/stops/0380E283I250")
    try:
        soup = BeautifulSoup(html_text.content, "lxml")
        thamesValleyBus = soup.find("li", class_="departure-board__item")
        thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

        stringInfo = thamesValleyNextBus.text.split()
        print(stringInfo)

        vandykeNorthService = 0
        vandykeNortharrival = 0
        vandykeNorthtime = 0

        # Check if the website's bus infomation is showing minutes or time

        for i in range(8, len(stringInfo)):
            if stringInfo[i] == "mins.":
                vandykeNorthService = stringInfo[2]
                vandykeNortharrival = stringInfo[i - 1]
                vandykeNorthtime = TimeAdd(current_time, vandykeNortharrival)
                break

            if stringInfo[i] == "min.":
                vandykeNorthService = stringInfo[2]
                vandykeNortharrival = stringInfo[i - 1]
                time = TimeAdd(current_time, vandykeNortharrival)
                break

            if stringInfo[i] == "Due.":
                vandykeNorthService = stringInfo[2]
                vandykeNortharrival = 0
                time = current_time
                break

        if vandykeNortharrival == 0 and vandykeNorthtime == 0:
            vandykeNorthService = stringInfo[2]
            vandykeNorthtime = stringInfo[11]
            vandykeNorthtime = vandykeNorthtime[:-1]
            vandykeNortharrival = TimeDifference(current_time, vandykeNorthtime)

        print(
            f"""
            (Vandyke North Bound Bus Stop) Next Bus Information:
            Service: {vandykeNorthService}
            Time: {vandykeNorthtime}
            Arrival: {vandykeNortharrival} Minutes
            """
        )

    except:
        print("HELP")

    list = [vandykeNorthService, vandykeNorthtime, vandykeNortharrival]
    return list


def vandykeSouthBoundScrape():
    # TIME
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)

    # VANDYKE SOUTH BOUND READING LION 4 BUS
    html_text = requests.get("https://www.reading-buses.co.uk/stops/0380E293I261")

    try:
        soup = BeautifulSoup(html_text.content, "lxml")
        thamesValleyBus = soup.find("li", class_="departure-board__item")
        thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

        stringInfo = thamesValleyNextBus.text.split()
        vandykeSouthService = 4

        vandykeSoutharrival = 0
        vandykeSouthtime = 0

        # Check if the website's bus infomation is showing minutes or time
        for i in range(8, len(stringInfo)):
            if stringInfo[i] == "mins.":
                vandykeSoutharrival = stringInfo[i - 1]
                vandykeSouthtime = TimeAdd(current_time, vandykeSoutharrival)
                break

            if stringInfo[i] == "min.":
                vandykeSoutharrival = stringInfo[i - 1]
                time = TimeAdd(current_time, vandykeSoutharrival)
                break

            if stringInfo[i] == "Due.":
                vandykeSoutharrival = 0
                time = current_time
                break

        if vandykeSoutharrival == 0 and vandykeSouthtime == 0:
            vandykeSouthtime = stringInfo[10]
            vandykeSouthtime = vandykeSouthtime[:-1]
            vandykeSoutharrival = TimeDifference(current_time, vandykeSouthtime)

        print(
            f"""
            (Vandyke South Bound Bus Stop) Next Bus Information:
            Service: {vandykeSouthService}
            Time: {vandykeSouthtime}
            Arrival: {vandykeSoutharrival} Minutes
            """
        )

    except:
        print("HELP")

    list = [vandykeSouthService, vandykeSouthtime, vandykeSoutharrival]
    return list


def ullswaterNorthBoundScrape():
    # TIME
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)

    # THAMES VALLEY BUS ULLSWATER NORTH BOUND
    html_text = requests.get("https://www.thamesvalleybuses.com/stops/0380E413J975")

    try:
        soup = BeautifulSoup(html_text.content, "lxml")
        thamesValleyBus = soup.find("li", class_="departure-board__item")
        thamesValleyNextBus = thamesValleyBus.find("p", class_="sr-only")

        stringInfo = thamesValleyNextBus.text.split()
        ullswaterNorthservice = stringInfo[2]

        ullswaterNortharrival = 0
        ullswaterNorthtime = 0

        # Check if the website's bus infomation is showing minutes or time

        for i in range(8, len(stringInfo)):
            if stringInfo[i] == "mins.":
                ullswaterNortharrival = stringInfo[i - 1]
                ullswaterNorthtime = TimeAdd(current_time, ullswaterNortharrival)
                break

            if stringInfo[i] == "min.":
                ullswaterNortharrival = stringInfo[i - 1]
                time = TimeAdd(current_time, ullswaterNortharrival)
                break

            if stringInfo[i] == "Due.":
                ullswaterNortharrival = 0
                time = current_time
                break

            # if last element in list doesn't contain the words 'mins.', Will assume it's a time not a duration
            # stringInfo[11] is hard coded, idc LOL. But every 11th element should include the time.
            # else:
            #     ullswaterNorthtime = stringInfo[11]
            #     ullswaterNorthtime = ullswaterNorthtime[:-1]
            #     ullswaterNortharrival = TimeDifference(current_time, ullswaterNorthtime)

        if ullswaterNortharrival == 0 and ullswaterNorthtime == 0:
            ullswaterNorthtime = stringInfo[11]
            ullswaterNorthtime = ullswaterNorthtime[:-1]
            ullswaterNortharrival = TimeDifference(current_time, ullswaterNorthtime)

        print(
            f"""
            (Ullswater North Bound Bus Stop) Next Bus Information:
            Service: {ullswaterNorthservice}
            Time: {ullswaterNorthtime}
            Arrival: {ullswaterNortharrival} Minutes
            """
        )

    except:
        print("HELP")

    list = [ullswaterNorthservice, ullswaterNorthtime, ullswaterNortharrival]
    return list
