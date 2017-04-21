#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,time
off = raw_input("Deseas comenzar la sugarizacion? (si, no o ayuda)")

time.sleep(3)
if off == "si":
	print "Responde las preguntas"
	os.system("chmod +x *")
	os.system("chmod +x Sugarizar\ software/*")
	os.system("./libcanberra-logout-sound.sh")
	os.system("./Sugarizar\ software/sug")
if off == "no":
	print "Hasta luego..."
	os.system("sudo poweroff")
if off == "ayuda":
	print "Responde las preguntas" 
	print "Luego reinicia el sistema"
	print "Despues copia el programa linux (application/executable) a la carpeta bin de la actividad"
	print "Por ultimo reinicia y listo"
	time.sleep(15)
	os.system("exit")
