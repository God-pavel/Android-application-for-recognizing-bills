import face_recognition
from PIL import Image, ImageDraw

# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.


# Load a second sample picture and learn how to recognize it.
one_image = face_recognition.load_image_file("one.jpg")
one_face_encoding = face_recognition.face_encodings(one_image)[0]

# two_image = face_recognition.load_image_file("two.jpg")
# two_face_encoding = face_recognition.face_encodings(two_image)[0]

# Load a sample picture and learn how to recognize it.
five_image = face_recognition.load_image_file("five1.jpeg")
five_face_encoding = face_recognition.face_encodings(five_image)[0]

ten_image = face_recognition.load_image_file("ten.jpeg")
ten_face_encoding = face_recognition.face_encodings(ten_image)[0]

twenty_image = face_recognition.load_image_file("twenty.jpg")
twenty_face_encoding = face_recognition.face_encodings(twenty_image)[0]

fifty_image = face_recognition.load_image_file("fifty.jpg")
fifty_face_encoding = face_recognition.face_encodings(fifty_image)[0]

hundred_image = face_recognition.load_image_file("hundred.jpg")
hundred_face_encoding = face_recognition.face_encodings(hundred_image)[0]

twoh_image = face_recognition.load_image_file("twoh.jpg")
twoh_face_encoding = face_recognition.face_encodings(twoh_image)[0]

fiveh_image = face_recognition.load_image_file("fiveh.jpeg")
fiveh_face_encoding = face_recognition.face_encodings(fiveh_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    fiveh_face_encoding,
    one_face_encoding,
    # two_face_encoding,
    five_face_encoding,
    ten_face_encoding,
    twenty_face_encoding,
    fifty_face_encoding,
    hundred_face_encoding,
    twoh_face_encoding,
]
known_face_names = [
    "Fifty grn",
    "One grn",
    # "Two grn",
    "Five grn",
    "Ten grn",
    "Twenty grn",
    "Hundred grn",
    "Two hundred grn",
    "Five hundred grn",
]

# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("fiveh.jpeg")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        print(matches)
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")
