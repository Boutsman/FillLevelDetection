import imgproc
from imgproc import *
# Import komt van https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/image-processing/intro.html
# ALTIJD EERST VOLGENDE SCRIPT TYPEN
# WARNING: Indien error: sudo modprobe bcm2835-v4l2


# 200x800px waren de begininstellingen voor te testen, nadien aangepast voor sneller systeem
width =  100 
height = 400

# Instelbare hoogte, wanneer is de fles wijn genoeg gevuld
# Dit moet in een latere versie volledig zelfstandig kunnen gebeuren
height_wine =  185


# Camera en viewer openen
camera = Camera(width, height)
viewer = Viewer(width, height, "Bottlemachine")

# Foto nemen en tonen via viewer
img = camera.grabImage()
preview = camera.grabImage()

# Een blauwe lijn trekken waar het vloeistofoppervlak boven moet liggen
for x in range (0, preview.width):
	preview[x, height_wine -1] = 0, 0, 255
	preview[x, height_wine] = 0, 0, 255
	preview[x, height_wine +1] = 0, 0, 255

viewer.displayImage(preview)

# FUTURE TODO
# Deze functie kan de vorm bepalen van de fles
# If green > 150 and red > 150 and blue > 150


# iterate over each pixel in the image
for x in range (0, img.width):
	for y in range (0, img.height):
		red, green, blue = img[x, y]

		if blue > green and blue > red and blue < 190:
			# Change colour to black
			img[x, y] = 0, 0, 0
		else:
			# Change colour to white
			img[x, y] = 255, 255, 255


# Instellingen voor de lijn met meeste zwarte pixels te bepalen
countblack = 0
maxIndex = 0
max = 0

# Deze functie bepaalt welke lijn de meeste zwarte pixels heeft en hoeveel deze zijn
for y in range (0, img.height):
	for x in range (0, img.width):
		# Aangezien we zwart wit gebruiken, moeten we maar naar 1 ding kijken vb of groen 255 of 0 is
		red, green, blue = img[x, y]

		# Tel het aantal zwarte pixels per rij
		if red < 1 and green < 1 and blue < 1:
			countblack += 1
			if countblack > max:
				max = countblack
				maxIndex = y
			else:
				pass
		else:
			pass
	# Lijst terug 0 maken, anders wordt alles opgeteld
	countblack = 0

print "Op lijn", maxIndex, "zijn de meeste zwarte pixels aanwezig."
print "Op deze lijn bevinden zich", max, "zwarte pixels."

if maxIndex < height_wine:
	print "De fles is VOLDOENDE gevuld."

	# Een groene lijn trekken van 3px dik, op het vloeistofoppverlak
	for x in range (0, img.width):
		img[x, maxIndex -1] = 0, 255, 0
		img[x, maxIndex] = 0, 255, 0
		img[x, maxIndex +1] = 0, 255, 0
else:
	print "De fles is ONVOLDOENDE gevuld."

	# Een rode lijn trekken van 3px dik, op het vloeistofoppverlak
	for x in range (0, img.width):
		img[x, maxIndex -1] = 255, 0, 0
		img[x, maxIndex] = 255, 0, 0
		img[x, maxIndex +1] = 255, 0, 0

# Een blauwe lijn trekken waar het vloeistofoppervlak boven moet liggen
for x in range (0, img.width):
	img[x, height_wine -1] = 0, 0, 255
	img[x, height_wine] = 0, 0, 255
	img[x, height_wine +1] = 0, 0, 255

viewer.displayImage(img)

# Voor lang genoeg te kijken wat er is gebeurd
waitTime(10000)
