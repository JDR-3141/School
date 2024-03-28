from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import mm

canvas = Canvas("hello_world.pdf")
canvas.drawString(72, 72, "Hello World!")
#for i in range(590,610,1): # Working out the width - it's 595
#    canvas.line(0,(i%590+1)*10,i,(i%590+1)*10)
#for i in range(840,850,1): # Working out the height - it's 842
#    canvas.line((i-830)*10,0,(i-830)*10,i)
for i in range(5): # Drawing the staff
    canvas.line(20,832-i*(1.75*mm),575,832-i*(1.75*mm))
canvas.ellipse(100,832-1.75*mm,104,832-3.5*mm) # using ellipse to draw note
canvas.line(100,832-1.75*mm,100,812-1.75*mm)
canvas.arc(200,200,203,205)
canvas.arc(203,205,200,200)
canvas.line(0,0,210*mm, 297*mm)
canvas.drawImage("Small_crotchet.png", 250,400)
canvas.save()