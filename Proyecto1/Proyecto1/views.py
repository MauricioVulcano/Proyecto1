from django.http import HttpResponse
import datetime
from django.template import Template,Context,loader # el loader sirve para parametrizar la ruta


#def saludo(request):
    #return HttpResponse("Hola Django equipo coder")

def saludo(request):
    return HttpResponse("Hola")

def segundaVista(request):
    return HttpResponse("<br><br> <h1>Hola mundo!</h1>")

def diaDeHoy (request):
    dia = datetime.datetime.now()

    documentoDeTexto = f"El dia de hoy es {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs (self,nombre): # en este caso, cuando entremos al puerto, para que retorne el nombre la URL seria http://127.0.0.1:8000/miNombreEs/<nombre>
    data = f"Mi nombre es: <h1>{nombre}</h1>"
    return HttpResponse(data) 

def probandoTemplate (self): 
    nombre = "Mauricio"
    apellido = "Vulcano"

    nameList = [
        "Gabriel", "Jimena", "Ignacio", "Patricia", "Natalia"
    ]

    diccionario = {
        "nombre" : nombre,
        "apellido" : apellido,
        "nameList" : nameList
    }




    #miHTML = open("C:/Proyectos/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html") 
    #plantilla = Template(miHTML.read()) direccion donde apunta la template en caso de no tenerlo configurado desde dir
    # miHTML.close() # se cierra para no consumir memoria si abro directamente el archivo con open
    # miContext = Context(diccionario) la dejamos vacia porque no tenemos nada que ponerle al HTML de contenido. Informacion que puede llegar a tener la templeta, esta puede recibir variables. En caso de configurarlo desde DIR se deja de renderizar asi y en render se envia el diccionario completo, por dejar de utilizar el open
    #documento = plantilla.render(miContext) el render es pintar. Documento es el producto terminado entre la combinacion del template y el contexto, donde el template almacena la informacion del contexto respectivamente ordenada donde queremos almacenar esa informacion
    # return HttpResponse(documento)

    plantilla = loader.get_template("template1.html") # se configura en setting DIR[]
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
    



