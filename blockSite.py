import sys

def bloquear(url):
	#Funcion para agregar URL en archivo hosts
	try:
		if url[4] == "s":
			url = url[8:]
		
		elif url[4] == ":":
			url = url[7:]
		
		barra = url.find("/")
		url = url[:barra]
		hosts = open("C:\Windows\System32\drivers\etc\hosts","a")
		hosts.write("127.0.1.1 \t" + url + "\n")
		hosts.close()
		print("URL Agregada")
	except:
		print("Se ha producido un error.")

bloquear(sys.argv[1])