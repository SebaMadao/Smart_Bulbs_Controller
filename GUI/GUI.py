import PySimpleGUI as sg
import GUI_events


def make_window():
    theme = 'DarkGrey15'
    sg.theme(theme)
    space_for_layout_online_bulbs_right = 10

    def set_name_with_space(name, name_space):
        spaces = name_space - len(name) - 2
        return sg.Text(name + ' ' + ' ' * spaces, size=(name_space, 1), justification='r', pad=(0, 0),
                       font='Courier 10')

    layout_online_bulbs_left = [[sg.Button('Search bulbs', expand_x=True, key='-BUTTON-SEARCH-BULBS-')],
                                [sg.Listbox(values=['Example_bulb_1', 'Example_bulb_2', 'Example_bulb_3'],
                                            expand_y=True, expand_x=True, enable_events=True,
                                            key='-LISTBOX-SEARCH-BULBS-', size=(30, 10))]
                                ]

    layout_online_bulbs_right = [[sg.Text("Bulb's properties:", size=(25, 1), justification='center',
                                          font=("Helvetica", 12), relief=sg.RELIEF_RIDGE, expand_x=True)],
                                 [set_name_with_space('Power:', space_for_layout_online_bulbs_right),
                                  sg.Text("NO DATA", key='-TEXT-POWER-STATUS-')],
                                 [set_name_with_space('Bright:', space_for_layout_online_bulbs_right),
                                  sg.Text("NO DATA", key='-TEXT-BRIGHT-STATUS-')],
                                 [sg.Text("RGB Color:", size=(25, 1), justification='center',
                                          font=("Helvetica", 10), relief=sg.RELIEF_RIDGE, expand_x=True)],
                                 [sg.Text("NO DATA", key='-TEXT-RGB-COLOR-STATUS-')],
                                 [sg.Text("Color temperature:", size=(25, 1), justification='center',
                                          font=("Helvetica", 10), relief=sg.RELIEF_RIDGE, expand_x=True)],
                                 [sg.Text("NO DATA", key='-TEXT-COLOR-TEMPERATURE-STATUS-')]
                                 ]

    layout_online_bulbs = [[sg.Column(layout_online_bulbs_left, p=0, expand_y=True, expand_x=True),
                           sg.Column(layout_online_bulbs_right, p=0, expand_y=True, expand_x=True)]
                           ]

    layout = [[sg.Text('SMART BULBS CONTROLLER', size=(35, 1), justification='center', font=("Helvetica", 16),
                       relief=sg.RELIEF_RIDGE, expand_x=True)]
              ]

    layout += [[sg.TabGroup([[sg.Tab('Online Bulbs', layout_online_bulbs),
                              ]], expand_x=True, expand_y=True)
                ]]

    window = sg.Window('SMART BULBS CONTROLLER', layout, keep_on_top=False, grab_anywhere=True, resizable=True)
    return window


def start_gui():
    window = make_window()
    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event:
            pass

        if event == '-BUTTON-SEARCH-BULBS-':
            GUI_events.event_update_listbox_of_discovered_bulbs(window=window, key='-LISTBOX-SEARCH-BULBS-')

        if event == '-LISTBOX-SEARCH-BULBS-':
            if values['-LISTBOX-SEARCH-BULBS-']:
                if isinstance(values['-LISTBOX-SEARCH-BULBS-'][0], str):
                    pass
                else:
                    GUI_events.event_update_bulb_properties(window=window, bulb=values['-LISTBOX-SEARCH-BULBS-'][0],
                                                            key_power_status='-TEXT-POWER-STATUS-',
                                                            key_bright_status='-TEXT-BRIGHT-STATUS-',
                                                            key_rgb_color_status='-TEXT-RGB-COLOR-STATUS-',
                                                            key_color_temperature_status=
                                                            '-TEXT-COLOR-TEMPERATURE-STATUS-')

        if 'IF' in event:
            pass

    window.close()


if __name__ == '__main__':
    start_gui()