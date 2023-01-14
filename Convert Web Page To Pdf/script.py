# Import the necessary libraries
from selenium import webdriver
from PIL import Image
import PyPDF2 as pypdf2
import urllib
import io
from Screenshot import Screenshot_clipping
import pyautogui

 
#Check is this is a valid Web Page


# Test if the string is a URL
def is_url(string):
    try:
        result = urllib.parse.urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
# Open the web page in a browser

input_web_page=input("Tell Me The Web Site")
input_pdf_name=input("Tell me the file name")
buffer=io.BytesIO
if(is_url(input_web_page)):
    driver = webdriver.Chrome()
    driver.get(input_web_page)
    # Set Web Site To Load
    # Wait for the page to load
    driver.implicitly_wait(10)

    # Get the height of the page
    height = driver.execute_script("return Math.max( document.body.scrollHeight);")

    # Take multiple screenshots
    screenshots = []
    for i in range(0, height, 1000):
        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, {});".format(i))
        
        # Wait for the page to load
        driver.implicitly_wait(100)
        
        # Take a screenshot
        takeScreenshot = pyautogui.screenshot()
        screenshots.append(takeScreenshot)

    # Create a PDF from the screenshots
    pdf_buffer = io.BytesIO()
    pdf = pypdf2.PdfWriter()
    print(screenshots.count())
    for screenshot in screenshots:
        print(type(screenshot))
        # Convert the image to a PDF
        img = Image.open(io.BytesIO(screenshot))
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PDF')
        
        # Create a PDF page from the PDF data
        pdf_page = pypdf2.PdfReader(img_buffer).getPage(0)
        pdf.addPage(pdf_page)

    # Save the PDF to a file
    pdf.write(pdf_buffer)
    with open('screenshot.pdf', 'wb') as f:
        f.write(pdf_buffer.getbuffer())

    # Close the browser
    driver.quit()
else:
    print("please enter correct web page")
