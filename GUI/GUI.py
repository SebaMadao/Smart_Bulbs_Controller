import PySimpleGUI as sg
import GUI_events


def make_window():
    theme = 'DarkGrey15'
    sg.theme(theme)
    space_for_layout_online_bulbs_right = 15
    space_for_layout_online_bulbs_set_properties = 12

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
                                 [set_name_with_space('Color mode:', space_for_layout_online_bulbs_right),
                                  sg.Text("NO DATA", key='-TEXT-COLOR-MODE-STATUS-')],
                                 [sg.Text("RGB Color:", size=(25, 1), justification='center',
                                          font=("Helvetica", 10), relief=sg.RELIEF_RIDGE, expand_x=True)],
                                 [sg.Text("NO DATA", key='-TEXT-RGB-COLOR-STATUS-'),
                                  sg.Canvas(background_color=sg.theme_button_color()[1], size=(40, 20), expand_x=True,
                                            key='-CANVAS-RGB-COLOR-')],
                                 [sg.Text("Color temperature:", size=(25, 1), justification='center',
                                          font=("Helvetica", 10), relief=sg.RELIEF_RIDGE, expand_x=True)],
                                 [sg.Text("NO DATA", key='-TEXT-COLOR-TEMPERATURE-STATUS-'),
                                  sg.Canvas(background_color=sg.theme_button_color()[1], size=(40, 20), expand_x=True,
                                            key='-CANVAS-KELVIN-COLOR-')]
                                 ]

    layout_online_bulbs = [[sg.Column(layout_online_bulbs_left, p=0, expand_y=True, expand_x=True),
                            sg.Column(layout_online_bulbs_right, p=0, expand_y=True, expand_x=True)],
                           [sg.Text("Set bulb's properties:", size=(25, 1), justification='center',
                                    font=("Helvetica", 12), relief=sg.RELIEF_RIDGE, expand_x=True)],
                           [set_name_with_space('Power: ', space_for_layout_online_bulbs_set_properties),
                            sg.Button('NO DATA', expand_x=True, key='-BUTTON-SET-POWER-')],
                           [set_name_with_space('Bright: ', space_for_layout_online_bulbs_set_properties),
                            sg.Slider((1, 100), orientation='h', size=(10, 15), expand_x=True)],
                           [set_name_with_space('Temp: ', space_for_layout_online_bulbs_set_properties),
                            sg.Slider((1700, 6500), resolution=100, orientation='h', size=(10, 15), expand_x=True),
                            sg.Canvas(background_color=sg.theme_button_color()[1], size=(50, 30),
                                      key='-CANVAS-SET-KELVIN-COLOR-'),
                            sg.Button('Set', size=(8, 1), key='-BUTTON-SET-TEMP-COLOR-')],
                           [set_name_with_space('RGB: ', space_for_layout_online_bulbs_set_properties),
                            sg.Text('', expand_x=True),
                            sg.ColorChooserButton("Choose", border_width=1, size=(8, 1),
                                                  key='-COLOR-CHOOSER-BUTTON-SET-RGB-COLOR-'),
                            sg.Text("{'R': 0, 'G': 0, 'B': 0}", key='-TEXT-SET-RGB-COLOR-'),
                            sg.Button('Set', size=(8, 1), key='-BUTTON-SET-RGB-COLOR-')]
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
                                                            '-TEXT-COLOR-TEMPERATURE-STATUS-',
                                                            key_canvas_rgb_color='-CANVAS-RGB-COLOR-',
                                                            key_canvas_kelvin_color='-CANVAS-KELVIN-COLOR-',
                                                            key_color_mode_status='-TEXT-COLOR-MODE-STATUS-')

    window.close()


if __name__ == '__main__':
    start_gui()
