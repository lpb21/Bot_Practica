from pywinauto.application import Application


# puede ser uia o en caso de error tambien puede ser win32
#.start y la ruta, o ejecutable del archivo en etste caso es el bloc de notas
#se puede ejecutar junto con la conexion en la misma linea
Application = Application(backend="uia").start("notepad.exe",timeout=5)#.connect(title="Link de prueba php_new.txt - notepad",timeout=20)

#conecta con un archivo ya creado
#Application = Application(backend="uia").connect(title="Untitled- Notepad")