from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def create_pdf(images, output_pdf):
    # Create a PDF document
    pdf = canvas.Canvas(output_pdf, pagesize=letter)

    print("Creating PDF...")

    for image_path in images:
        # Open the image using Pillow
        img = Image.open(image_path)

        # Get the size of the image and the size of the PDF page
        img_width, img_height = img.size
        pdf_width, pdf_height = letter

        # Calculate the aspect ratio of the image
        aspect_ratio = img_width / img_height

        # Calculate the width and height for the image on the PDF page
        if aspect_ratio > 1:
            width = pdf_width
            height = pdf_width / aspect_ratio
        else:
            width = pdf_height * aspect_ratio
            height = pdf_height

        # Draw the image on the PDF page
        pdf.drawInlineImage(img, 0, 0, width, height)

        # Add a new page for the next image
        pdf.showPage()

        print("Added {} to PDF".format(image_path))

    # Save the PDF
    print("Saving PDF")
    pdf.save()
    print("PDF saved to {} (time = {})".format(output_pdf))

def scan_images_recursively(directory):
    # Scan the directory recursively for images
    image_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                image_paths.append(os.path.join(root, file))
    return image_paths

# os folder browser use pyqt5
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys

# mac os
image_paths = scan_images_recursively(folder_selected)
output_pdf_path = os.path.join(destination, "output.pdf")

create_pdf(image_paths, output_pdf_path)
# print(image_paths)