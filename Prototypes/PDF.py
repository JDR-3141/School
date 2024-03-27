from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("hello_world.pdf")
canvas.drawString(72, 72, "Hello World!")
#for i in range(590,610,1): # Working out the width - it's 595
#    canvas.line(0,(i%590+1)*10,i,(i%590+1)*10)
#for i in range(840,850,1): # Working out the height - it's 842
#    canvas.line((i-830)*10,0,(i-830)*10,i)
for i in range(5): # Drawing the staff
    canvas.line(20,832-i*5,575,832-i*5)
canvas.ellipse(101,101,103,104)
canvas.save()