from PIL import Image

# 🛡️ Disable the decompression bomb protection (safe here)
Image.MAX_IMAGE_PIXELS = None

# 📂 Load and view the image
img = Image.open(r"C:\Users\USER\projects\helloworld\Code_Practice\Computer_Graphics\cube.ppm")
img.show()
