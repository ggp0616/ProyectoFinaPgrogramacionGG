import qrcode
data = "Proyecto Final para la presentación del 28/11"
img = qrcode.make(data)
img.save("C:/Users/alumnos/Desktop/GuadaGallardo/ProyectoFinalPgrogramacion-GG/myqrcode.png")