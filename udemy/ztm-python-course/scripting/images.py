from PIL import Image, ImageFilter

img = Image.open('./images/bunger.png')
filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("blur.png", "png")
converted_img = img.convert("L")
rotated = converted_img.rotate(90)
resize = converted_img.resize((300, 300))
cropped = img.crop((100, 100, 400, 400))
rotated.save("./images/bw_bunger.png", "png")
