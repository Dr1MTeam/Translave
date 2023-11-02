import easyocr


def text_recognition(file_path):
    reader = easyocr.Reader(["ru", "en"])
    result =reader.readtext(file_path, detail=0)

    return result


file_path = 'assets/new_image.jpg'
print(text_recognition(file_path=file_path))