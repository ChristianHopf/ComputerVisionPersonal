from PIL import Image
from PIL import ImageOps


# Given an image and kernel, returns the image convolved with the kernel.
# A kernel is a square 2D array.
def convolve(image, kernel, stride=None):
    image.show()
    output = Image.new('RGB', (image.width, image.height), color=0)  # create a black output image of original size

    # loop over each pixel in the original image
    for x in range(image.width):
        for y in range(image.width):
            # at each pixel, calculate the value of the output image at that pixel by applying the kernel to that
            # neighborhood of pixels
            new_pixel = 0
            for u in range(-1, 1):
                for v in range(-1, 1):
                    new_pixel += kernel[1 + u][1 + v] * image.getpixel((x + u, y + v))
            output.putpixel((x, y), (new_pixel, new_pixel, new_pixel))
    output.show()
    name = str(image) + "_convolved"
    output.save(name)


if __name__ == "__main__":
    identity_kernel = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    jermasus = ImageOps.grayscale(Image.open('images/JermaSus.jpg'))
    print(jermasus.getpixel((20, 20)))
    convolve(jermasus, identity_kernel)
