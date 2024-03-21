from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("hello_world.pdf")
canvas.drawString(72, 72, "Hello World!")
canvas.line(0,0,100,100)
canvas.save()