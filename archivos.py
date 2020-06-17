#!/usr/bin/python3

from datetime import date
import sys, getopt
import os

def main(argv):
    input_file = ""
    output_file = ""
    filas = 0
    num_errores = 0;
    guia = " \n"
    last_line = " "
    last2_lines = " "
    last3_lines = " "
    last4_lines = " "
    clean_line = 0
    error_dict = {}

    fecha = date.today()
    hoy = fecha.strftime("%m-%d-%Y")

    mes_archivo(hoy)
    print(mes_archivo(hoy))

  
    input_file = eval(input("caca: "))
            
    output_file =  mes_archivo(hoy) + "/" + input("Archivo que desea crear: ")  + str(hoy) + ".txt"

    with open(input_file, "rt") as file:
        lines = list(file.readlines())
        percentage_unit = round(len(lines)/100)

        while filas < len(lines):
            line = lines[filas]
            clean_line += 1

            if ("Cima" in line or "PILA" in line) and "Cola" in line:
                guia = line

            elif "ERROR" in line:
                num_errores += 1
                clean_line = 0
                error = get_error_name(line)

                if error in error_dict:
                    error_dict[error] +=  1
                else:
                    error_dict.update({error: 1})

                is_first_error_ingreso = "ingreso" in error and error_dict[error] == 1

                if ("CACHESAVE" and "cima" not in line or is_first_error_ingreso):
                    imprimir_error(output_file, num_errores, filas, guia, lines)

                elif ("CACHESAVE" and "Tweet" in line):
                    imprimir_error(output_file, num_errores, filas, guia, lines)



            last4_lines = last3_lines
            last3_lines = last2_lines
            last2_lines = last_line
            last_line = line

            if(filas%(percentage_unit*10) == 0):
                print(str(round(filas/percentage_unit)) + "%")

            filas+=1
    print_results(error_dict, output_file)



def mes_archivo(hoy):
    mes = hoy[:2]
    año = hoy[6:]

    if int(mes) == 1:
        mes = "ENERO"
        os.makedirs( mes + año ,exist_ok=True)

    elif int(mes) == 2:
        mes = "FEBRERO"
        os.makedirs( mes + año ,exist_ok=True)

    elif int(mes) == 3:
        mes = "MARZO" + año
        os.makedirs( mes, exist_ok=True)

    elif int(mes) == 4:
        mes = "ABRIL" + año
        os.makedirs( mes,exist_ok=True)

    elif int(mes) == 5:
        mes = "MAYO" + año
        os.makedirs( mes ,exist_ok=True)

    elif int(mes) == 6:
        mes = "JUNIO" + año
        os.makedirs( mes ,exist_ok=True)

    elif int(mes) == 7:
        mes = "JULIO" + año
        os.makedirs( mes ,exist_ok=True)

    elif int(mes) == 8:
        mes = "AGOSTO"
        os.makedirs( mes + año ,exist_ok=True)

    elif int(mes) == 9:
        mes = "SEPTIEMBRE"
        os.makedirs( mes + año ,exist_ok=True)
    elif int(mes) == 10:
        mes = "OCTUBRE"
        os.makedirs( mes + año ,exist_ok=True)

    elif int(mes) == 11:
        mes = "NOVIEMBRE"
        os.makedirs( mes + año ,exist_ok=True)

    elif int(mes) == 12:
        mes = "DICIEMBRE"

        os.makedirs( mes + año ,exist_ok=True)

    else:
        mes = "MES INVALIDO"
        os.makedirs( mes + año ,exist_ok=True)

    return(mes)




def imprimir_error(output_file, num_errores, num_linea, guia, lineas):
    text_file = open(output_file, "a")
    error = "\n\n" + str(num_errores) + ".- " + guia + "\n"
    i = num_linea - 3
    while i < num_linea + 3:
        error += "#Linea" + str(i) + ": " + lineas[i]
        i+= 1
    n = text_file.write(error)

def get_error_name(line):
    error_name = line.replace("\n", "")
    error_name = error_name.replace("ERROR:root:", "")
    if "Fecha" in line:
        error_name = error_name[33:]

    elif "CACHESAVE" and "host" in line:
        keyword = "host"
        last_char = error_name.index(keyword) + len(keyword)
        error_name = error_name[0:last_char]

    elif "CACHESAVE" and "it" in line:
        keyword = "it"
        last_char = error_name.index(keyword) + len(keyword)
        error_name = error_name[0:last_char]
        


    elif "CACHESAVE" and "cima" in error_name:
        keyword = "cima"
        last_char = error_name.index(keyword) + len(keyword)
        error_name = error_name[0:last_char]

    elif "Name Threading" in error_name:
        keyword = "referenced before assignment"
        last_char = error_name.index(keyword) + len(keyword)
        error_name = error_name[0:last_char]

    return(error_name)

def print_results(error_dict, output_file):
    text_file = open(output_file, "a")
    newline = "\n"
    n = text_file.write(newline)
    for error_name, error_count in error_dict.items():
        text_file = open(output_file, "a")
        analizis = error_name + " : " + str(error_count) + "\n"
        print(analizis)
        n = text_file.write(analizis)



main(sys.argv[1:])
