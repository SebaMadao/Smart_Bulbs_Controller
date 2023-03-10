

def get_rgb_from_decimal(decimal_color):
    decimal_color = int(decimal_color)
    rgb_color = {'R':0, 'G':0, 'B':0}
    rgb_color['R'] = int(decimal_color / 65536)
    rgb_color['G'] = int((decimal_color - rgb_color['R'] * 65536)/256)
    rgb_color['B'] = int(decimal_color - rgb_color['R'] * 65536 - rgb_color['G'] * 256)
    return rgb_color


def get_decimal_from_rgb(rgb_color={'R': 0, 'G': 0, 'B': 0}):
    return rgb_color['B'] * 65536 + rgb_color['G'] * 256 + rgb_color['R']


def get_hex_from_rgb(rgb_color={'R': 0, 'G': 0, 'B': 0}):
    return '#%02x%02x%02x' % (rgb_color['R'], rgb_color['G'], rgb_color['B'])


def get_hex_from_decimal(decimal_color):
    return get_hex_from_rgb(get_rgb_from_decimal(decimal_color=decimal_color))


def get_rgb_from_hex(hex_color):
    hex_color = hex_color.lstrip('#')
    return {'R': int(hex_color[0:2], 16), 'G': int(hex_color[2:4], 16), 'B': int(hex_color[4:6], 16)}


if __name__ == '__main__':
    ''' rgb R:255 G:255 B:255 = decimal(16777215)'''
    print(f'16777215 decimal should be R:255 G:255 B:255 : {get_rgb_from_decimal(decimal_color=16777215)}')
    print(f"R:255 G:255 B:255 should be 16777215 decimal: "
          f"{get_decimal_from_rgb(rgb_color={'R':255, 'G':255, 'B':255})}")
    print(f"R:255 G:255 B:255 should be #FFFFFF  HEX: "
          f"{get_hex_from_rgb(rgb_color={'R':255, 'G':255, 'B':255})}")
    print(f"16777215 decimal should be #FFFFFF  HEX: "
          f"{get_hex_from_decimal(decimal_color=16777215)}")
    print(f"#FFFFFF HEX should be : R:255 G:255 B:255 RGB"
          f"{get_rgb_from_hex('#ffffff')}")


