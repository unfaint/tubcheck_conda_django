from PIL import Image
from tubcheck import ml_model


def handle_uploaded_file(f):
    print(3)
    with open('tmp/image.jpg', 'wb+') as fp:

        for chunk in f.chunks():
            print(type(chunk), type(f))
            fp.write(chunk)

    with open('tmp/image.jpg', 'rb') as fp:
        image = Image.open(fp)
        print(image)
        output = ml_model(image)

    return output
