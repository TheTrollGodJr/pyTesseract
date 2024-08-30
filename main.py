from PIL import Image
import pytesseract
#C:\Users\thetr\AppData\Local\Programs\Tesseract-OCR

# Path to the Tesseract executable (replace with your path) Paine-Age of Reason
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\thetr\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pageCount = 0
text = []

def image_to_text(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Replace 'path/to/your/image.png' with the actual path to your image file
image_path = 'C:/Users/thetr/Downloads/output/'
#titlePage = image_to_text(image_path)
#print("Title Page Done")
#'''
for i in range(16): 
    result_text = image_to_text(f"{image_path}{pageCount}.jpg")
    text.append(result_text)
    print(f"Page {pageCount} Done")
    pageCount += 1

# Print the extracted text
#print(result_text)
#'''
#'''
pageCount = 1
with open("PyTesseract/output.txt", "a") as f:
    #f.write(titlePage)
    for items in text:
        f.write(f"Page {pageCount}\n")
        pageCount += 1
        f.write(items)
        f.write("\n")
#'''
