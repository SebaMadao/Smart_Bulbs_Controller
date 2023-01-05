import Engine.Bulbs_search
import Engine.RGB_Decimal


def event_update_listbox_of_discovered_bulbs(window, key, bulbs_list=Engine.Bulbs_search.get_list_of_bulbs()):
    window[key].update(bulbs_list)


def event_update_bulb_properties(window, key_power_status, key_bright_status, key_rgb_color_status,
                                 key_color_temperature_status, bulb):
    bulb_properties = bulb.get_properties()
    window[key_power_status].update(bulb_properties['power'])
    window[key_bright_status].update(bulb_properties['bright'])
    window[key_rgb_color_status].update(Engine.RGB_Decimal.get_rgb_from_decimal(bulb_properties['rgb']))
    window[key_color_temperature_status].update(bulb_properties['ct'])
