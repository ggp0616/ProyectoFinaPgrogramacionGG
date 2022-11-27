import qrcode
data = 'https://www.youtube.com/watch?v=cQRTzL6Ui3w'   #"Proyecto Final para la presentación del 28/11"
img = qrcode.make(data)
img.save('Proyectos/fotitoRePiolaDelSapitoPepe.png')
img.show()