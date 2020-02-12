from PIL import Image

# Function to change the image size
def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage
    
# Take two images for blending them together   
image1 = Image.open("frame_82.JPG")

image2 = Image.open("frame82.JPG")
width, height = image2.size

print(height,width)

image2 = image2.crop((0, 461, width-0, height-0))
print(image2.size)
#image3.save("new.png","PNG")

# Make the images of uniform size
image3 = changeImageSize(1640, 461, image1)
image4 = changeImageSize(1640, 461, image2)

# Make sure images got an alpha channel
image5 = image1.convert("RGBA")
image6 = image2.convert("RGBA")

# Display the images
image1.show()
image2.show()

# alpha-blend the images with varying values of alpha
alphaBlended1 = Image.blend(image5, image6, alpha=.4)
alphaBlended2 = Image.blend(image5, image6, alpha=.2)

# Display the alpha-blended images
alphaBlended1.show()
alphaBlended2.show()

