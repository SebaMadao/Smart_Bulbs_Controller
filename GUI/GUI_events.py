import Engine.Bulbs_search
import Engine.Color_translation
import Engine.Kelvin_color


def event_update_listbox_of_discovered_bulbs(window, key, bulbs_list=Engine.Bulbs_search.get_list_of_bulbs()):
    window[key].update(bulbs_list)


def event_update_bulb_properties(window, key_power_status, key_bright_status, key_rgb_color_status,
                                 key_color_temperature_status, key_canvas_rgb_color, key_canvas_kelvin_color, bulb):
    bulb_properties = bulb.get_properties()
    window[key_power_status].update(bulb_properties['power'])
    window[key_bright_status].update(bulb_properties['bright'])
    window[key_rgb_color_status].update(Engine.Color_translation.get_rgb_from_decimal(bulb_properties['rgb']))
    window[key_color_temperature_status].update(bulb_properties['ct'])
    window[key_canvas_rgb_color].\
        update(background_color=Engine.Color_translation.get_hex_from_decimal(bulb_properties['rgb']))
    window[key_canvas_kelvin_color].update(background_color=Engine.Color_translation.get_hex_from_rgb(
        Engine.Kelvin_color.get_rgb_color_from_kelvin_temperature_color(int(bulb_properties['ct']))))

