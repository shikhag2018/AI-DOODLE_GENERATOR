from PIL import Image, ImageDraw
import json

with open('../complex-bracelets.json') as user_file:
  file_contents = user_file.read()

parsed_json = json.loads(file_contents)

suggested_drawings = parsed_json[0:10]

# print(suggested_drawings)

img = Image.new("RGB", (512, 512), (255, 255, 255))

# Draw the suggested doodles onto the image
draw = ImageDraw.Draw(img)
for drawing in suggested_drawings:
    for stroke in drawing["drawing"]:
        print(stroke)
        for i in range(len(stroke[0])-1):
            draw.line((stroke[0][i], stroke[1][i], stroke[0][i+1], stroke[1][i+1]), fill=(0, 0, 0), width=2)

# Save the image
img.save("doodle.png")