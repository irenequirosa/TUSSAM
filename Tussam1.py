from lxml import etree
from suds.client import Client
import suds

url='http://www.infobustussam.com:9001/services/dinamica.asmx?wsd1'
cliente = Client(url, retxml=True)
print '''
		Lineas de Tussam
'''
linea = raw_input("Linea :")
try:
			respuesta = cliente.service.GetStatusLinea(linea)
			print """
			"""
			
except suds.WebFault as error:
		print "Error la linea no existe"
	
else:
		raiz =etree.fromstring(respuesta)
		raiz2 = raiz [0][0]
		ns = "{http://tempuri.org/}"
		lineas_activos = raiz2.find(ns+"GetStatusLineaResult/"+ns+"activos")
		activos = lineas_activos.text
		lineas_frecuencia = raiz2.find(ns+"GetStatusLineaResult/"+ns+"frec_bien")
		buenafrec = lineas_frecuencia.text
		lineas_graves = raiz2.find(ns+"GetStatusLineaResult/"+ns+"graves")
		graves = lineas_graves.text
		
