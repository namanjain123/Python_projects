import os
import subprocess
import fitz
def remove_dependency(package_name):
    # Install the package without dependencies
    subprocess.check_call(['pip', 'install', '--no-deps',package_name])
def extract_images_from_pdf(pdf_file_path, output_folder_path):
    try:
        # Open the PDF file
        pdf_file = fitz.open(pdf_file_path)
        # Iterate over each page in the PDF file
        for page in pdf_file:
            # Extract all the images on the page
            images = page.getImageList()
            # Iterate over each image and save it as a high-resolution PNG file
            for i, image in enumerate(images):
                ref = image[0]
                pic = fitz.Pixmap(pdf_file, ref)
                if pic.n < 5:
                    # Convert the image to a RGB or RGBA format if necessary
                    pic.writePNG(os.path.join(output_folder_path, f'image_{page.number}_{i}.png'))
                else:
                    # For CMYK or similar images, convert them to RGB
                    pix1 = fitz.Pixmap(fitz.csRGB, pic)
                    pix1.writePNG(os.path.join(output_folder_path, f'image_{page.number}_{i}.png'))
                    pix1 = None
                pic = None
        return True
    except Exception as e:
        print(f"Error extracting images from PDF: {str(e)}")
        return False
try:
    print("Enter The Route of the pdf \n")
    route_pdf=input("\n")
    print("enter the images path \n")
    route_images=input("\n")
    result=extract_images_from_pdf(route_pdf,route_images)
    if result==True:
        print("Completed")
    else:
        print("error")
except Exception as e:
        print(f"Error")

