import webbrowser


def manage_maps(assistant):
    base_url = f"https://www.google.com/maps/search/?api=1"
    assistant.respond("What do you want to?")
    choice = ""
    while choice == "":
        choice = assistant.talk()

    if 'location search' in choice:
        assistant.respond("Give me place to search")
        place = assistant.talk()
        place = url_encode(place)
        url = base_url + f"&query={place}"
    elif 'categorical search' in choice:
        assistant.respond("Give me categorical place to search with location")
        place = assistant.talk()
        place = url_encode(place)
        url = base_url + f"&query={place}"
    elif 'directions' in choice:
        base_url = f"https://www.google.com/maps/dir/?api=1"
        assistant.respond("Give me origin")
        origin = assistant.talk()
        origin = url_encode(origin)
        assistant.respond("Give me destination")
        destination = assistant.talk()
        destination = url_encode(destination)
        assistant.respond("Give me travel mode. You can choose driving, walking, bicycling or transit")
        travel_mode = assistant.talk()
        travel_mode = url_encode(travel_mode)
        url = base_url + f"&origin={origin}&destination={destination}&travelMode={travel_mode}"
    else:
        assistant.respond("You didn't choose anything.")
        return
    webbrowser.open_new_tab(url)
    wait = ""
    while wait == "":
        wait = assistant.talk()


def url_encode(query):
    query = query.replace(" ", "+")
    query = query.replace("|", "%7C")
    query = query.replace(",", "%2C")
    query = query.lower()
    return query
