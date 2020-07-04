possible_vals = {'00', '55', 'aa', 'ff'}
color_codes = []

def gen_colors(value_set, size, color_codes):
    if size == 1:
        for val in value_set:
            color_codes.append(val)
        return color_codes
    else:
        for val in value_set:
            new_codes = []
            for new_val in gen_colors(value_set, size - 1, new_codes):
                color_codes.append(val + new_val)
        return color_codes
    
codes = gen_colors(possible_vals, 3, color_codes)

with open('swatches.html', 'w') as f:
    f.write('<html>\n')
    for code in codes:
        f.write('<a color=#' + code + '></a>\n')
    f.write('</html>\n')
