

def get_rgb_from_decimal(decimal_color):
    decimal_color = int(decimal_color)
    rgb_color = {'R':0, 'G':0, 'B':0}
    rgb_color['R'] = int(decimal_color / 65536)
    rgb_color['G'] = int((decimal_color - rgb_color['R'] * 65536)/256)
    rgb_color['B'] = int(decimal_color - rgb_color['R'] * 65536 - rgb_color['G'] * 256)
    return rgb_color


def get_decimal_from_rgb(rgb_color={'R':0, 'G':0, 'B':0}):
    return rgb_color['B'] * 65536 + rgb_color['G'] * 256 + rgb_color['R']


if __name__ == '__main__':
    ''' rgb R:255 G:255 B:255 = decimal(16777215)'''
    print(f'16777215 decimal should be R:255 G:255 B:255 : {get_rgb_from_decimal(decimal_color=16777215)}')
    print(f"R:255 G:255 B:255 should be 16777215 decimal: "
          f"{get_decimal_from_rgb(rgb_color={'R':255, 'G':255, 'B':255})}")

