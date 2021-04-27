from PIL import Image
import sys


def wraparoundHalf(img):
	w, h = img.size
	img2 = Image.new('RGB', (w, h))
	for y in range(h):
		for x in range(w):
			sx = (x + w / 2) % w
			sy = (y + h / 2) % h
			p = img.getpixel((sx, sy))
			img2.putpixel((x, y), p)
	return img2

def warparoundHalfImgFile(src, dst):
	img = Image.open(src)
	img2 = wraparoundHalf(img)
	img2.save(dst)

def main():
	warparoundHalfImgFile('test.png', 'out.png')

if __name__ == '__main__':
	sys.exit(main())
