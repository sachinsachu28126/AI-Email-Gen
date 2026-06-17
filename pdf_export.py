from reportlab.pdfgen import canvas

def create_pdf(text, filename="email.pdf"):
    c = canvas.Canvas(filename)
    y = 800

    for line in text.split("\n"):
        c.drawString(50, y, line[:100])
        y -= 20

    c.save()
    return filename