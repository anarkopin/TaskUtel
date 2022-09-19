
from metodos.metodos import *
from config.config import *
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException

def iniciar(usuario, contraseña, driver):
    try:
        # Automatizar logeo
        credenciales(usuario, contraseña, driver)
        menu(driver)

    except ElementNotVisibleException as e:
        print("Te has deslogeado o el elemento ya no existe")
        print("El programa se reiniciara")
        iniciar(driver, usuario, contraseña)

    except NoSuchElementException as e:
        print("Te has deslogeado o el elemento ya no existe")
        iniciar(driver, usuario, contraseña)


def menu(driver):
    id_crm= ""
    print()
    print("****************************************")
    print("********Bienvenido a task-UTEL**********")
    print("****************************************")
    print()
    print("Hola Soy Electron. Te voy ayudar a automatizar tus tareas de tipificacion, \n"
          "busqueda de prospectos vía idCrm \n"
          "y tambien busqueda de registros via correo\n"
          "todo esto mientras tu sigues llamando!")
    print()
    while (True):
        try:
            id_crm = str(input("Ingresa el id_crm a buscar: ")).strip()
            buscar_prospecto(id_crm,driver)
            driver.implicitly_wait(3)
            nombre_prospecto = driver.find_element_by_xpath('//*[@id="first_name"]').text

            if len(nombre_prospecto)==0:
                print("El idm_crm es erroneo o no le pertenece a ningun prospecto")
                continue
            else:
                while(True):
                    automatizar_tarea = int(input("""
                                El id_crm le pertenece a """+nombre_prospecto+"""\n
                                ***Que tarea quieres hacer con este id_crm?*** \n
                                1.Llenar datos \n 
                                2.Realizar Seguimiento \n
                                3.Buscar cliente con id_crm\n
                                4.Buscar registros con correo\n
                                5.Salir
                                """))

                    if (automatizar_tarea == 1):
                        descripcion = input("Que descripcion quieres poner?")
                        modificar_prospecto(driver, descripcion)
                    elif (automatizar_tarea == 2):
                        descripcion = input("Que descripcion quieres poner?")
                        seguimiento(driver, descripcion)
                    elif (automatizar_tarea == 3):
                        continue
                    elif (automatizar_tarea == 4):
                        correo = input("Ingresa el correo a buscar: ")
                        print("Consejo: Valida los registros y tipifica todos si es que es un seguimiento! \n"
                              "todavia no esta soportado la tipificacion de varios registros en diferentes pestañas!")
                        buscar_correo(correo, driver)
                        continue
                    elif automatizar_tarea==5:
                        quit()
                    else:
                        print("No existe tarea o todavia no haz colocado el id_crm")

        except ValueError:
            print("Escoge el numero correcto")

        except ElementNotVisibleException as e:
            print("Te has deslogeado o no se encontro id_crm o correo")
            print("El programa se reiniciara")
            credenciales(usuario,contraseña,driver)
            continue

        except NoSuchElementException as e:
            print("Te has deslogeado o no se encontro id_crm o correo")
            print("El programa se reiniciara")
            credenciales(usuario,contraseña,driver)
            continue




#DATOS LOGEO
archivo=open("contraseña.txt", "r")

datos = archivo.readlines()
usuario = datos[0]
contraseña = datos[1]



driver = driver()

iniciar(usuario, contraseña, driver)
















