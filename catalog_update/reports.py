#!/usr/bin/env python3

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import os

def generate_report(attachment, title, paragraph):
    c = canvas.Canvas(attachment, pagesize=letter)
    width, height = letter

    # Set the title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 40, title)

    # Set the paragraph
    c.setFont("Helvetica", 12)
    text = c.beginText(40, height - 80)
    text.setTextOrigin(40, height - 80)
    text.setFont("Helvetica", 12)
    text.textLines(paragraph)
    c.drawText(text)
    c.save()


