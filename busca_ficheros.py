import glob
import os


def busca_palabra(palabras, extesion):
    lista_de_ficheros = glob.glob(extesion)
    for fichero in lista_de_ficheros:
        fo = open(fichero)
        linea = fo.readline()
        encontrado = False
        while linea != "" and encontrado == False:
            for palabra in palabras:
                if(linea.find(palabra)>=0):
                    print("El fichero {} contiene la palabra {}".format(fichero,palabra))
                    encontrado = True                    
                    break
            linea = fo.readline()

os.chdir("C:/Users/manoel.alonso/Jedi")
busca_palabra(["Derecho Civil"],"*.csv")    
busca_palabra(["Derecho","Civil"],"*.csv")    

busca_palabra(["Python","Derecho"],"*.rtf")    

busca_palabra(["Curso"],"*.rtf")    

    

