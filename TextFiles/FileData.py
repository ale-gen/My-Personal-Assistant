def fetch_bye_commands():
    bye_commands = []
    with open('../TextFiles/bye_commands') as file:
        lines = file.readlines()
        for command in lines:
            bye_commands.append(command)
        file.close()
    return bye_commands


def fetch_help_commands():
    help_commands = []
    with open('../TextFiles/help_commands') as file:
        lines = file.readlines()
        for command in lines:
            help_commands.append(command)
        file.close()
    return help_commands


def get_api_keys():
    keys = {}
    with open('../TextFiles/apikeys') as file:
        body = file.readlines()
        for key in body:
            key = key.split(" ")
            keys.update({key[0]: key[1]})
        file.close()
    return keys