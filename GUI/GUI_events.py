import Engine.Bulbs_search
import Engine.Color_translation
import Engine.Kelvin_color
import yeelight


def event_update_listbox_of_discovered_bulbs(window, key, bulbs_list=Engine.Bulbs_search.get_list_of_bulbs()):
    window[key].update(bulbs_list)


def event_update_bulb_properties(window, key_power_status, key_bright_status, key_rgb_color_status,
                                 key_color_temperature_status, key_canvas_rgb_color, key_canvas_kelvin_color,
                                 key_color_mode_status, key_button_set_power, bulb):
    bulb_properties = bulb.get_properties()
    window[key_power_status].update(bulb_properties['power'])
    window[key_bright_status].update(bulb_properties['bright'])
    window[key_rgb_color_status].update(Engine.Color_translation.get_rgb_from_decimal(bulb_properties['rgb']))
    window[key_color_temperature_status].update(bulb_properties['ct'])
    window[key_canvas_rgb_color]. \
        update(background_color=Engine.Color_translation.get_hex_from_decimal(bulb_properties['rgb']))
    window[key_canvas_kelvin_color].update(background_color=Engine.Color_translation.get_hex_from_rgb(
        Engine.Kelvin_color.get_rgb_color_from_kelvin_temperature_color(int(bulb_properties['ct']))))
    window[key_color_mode_status].update((lambda x: 'RGB' if x == 1 else 'TEMP')(int(bulb_properties['color_mode'])))


def event_set_up_power(bulb):
    bulb_properties = bulb.get_properties()
    if bulb_properties['power'] == 'on':
        bulb.turn_off()
    else:
        bulb.turn_on()


def event_update_color_chooser_button(key_button):
    pass


def event_update_canvas_kelvin_color(key_canvas):
    pass


def event_set_up_bright(bulb, bright):
    bulb.set_brightness(int(bright))


def event_set_up_rgb_color(bulb):
    pass


def event_set_up_kelvin_color(bulb):
    pass

