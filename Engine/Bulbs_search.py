import yeelight


def get_list_of_bulbs():
    bulbs = []
    discovered_bulbs = yeelight.discover_bulbs()
    for discovered_bulb in discovered_bulbs:
        bulbs.append(yeelight.Bulb(discovered_bulb['ip']))
    return bulbs


if __name__ == '__main__':
    print(get_list_of_bulbs())
    for bulb in get_list_of_bulbs():
        print(bulb.get_properties())

