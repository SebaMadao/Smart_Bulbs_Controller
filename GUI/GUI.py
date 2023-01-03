import PySimpleGUI as sg


def make_window():
    theme = 'DarkGrey15'
    sg.theme(theme)

    layout = [[sg.Text('SMART BULBS CONTROLLER', size=(38, 1), justification='center', font=("Helvetica", 16),
                       relief=sg.RELIEF_RIDGE)]
              ]

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

        if event == '-START-BUTTON-':
            pass

        if 'IF' in event:
            pass

    window.close()


if __name__ == '__main__':
    start_gui()