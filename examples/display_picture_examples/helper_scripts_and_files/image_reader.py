from PIL import Image
import sys

def rgb2hex(rgb):
	r, g, b = rgb
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)
	
def rgb2dec(rgb):
	result = 0
	rgb_array = []
	for col in rgb:
		if col == 0:
			rgb_array.append(0)
		if col == 85:
			rgb_array.append(1)
		if col == 170:
			rgb_array.append(2)
		if col == 255:
			rgb_array.append(3)
	result += rgb_array[0] << 4
	result += rgb_array[1] << 2
	result += rgb_array[2]
	return result

def main():
	im = Image.open(sys.argv[1])
	pic_number = sys.argv[1].split('_')[0]
	pix = im.load()
	w, h = im.size

	dec_array = []
	xy_array = []

	for y in range(h):
		for x in range(w):
			xy_array.append((x << 5) + y)
			dec_array.append(rgb2dec(pix[x, y]))

	with open('draw_picture_{0}_header.asm'.format(pic_number), 'w') as f:
		for i in range(len(dec_array)):
			f.write('// color: {0}, xy: {1} {2}, index: {3}\n'.format(dec_array[i], xy_array[i] >> 5, xy_array[i] & 31, i))
			f.write('@64\n')
			f.write('D = A\n')
			f.write('@' + str(xy_array[i]) + '\n')
			f.write('D = D * A\n')
			f.write('@' + str(dec_array[i]) + '\n')
			f.write('S = D + A\n\n')
		
if __name__ == '__main__':
	main()