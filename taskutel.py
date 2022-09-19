from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
import os, time, random
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import init, Fore
from time import sleep



def credenciales(usuario, contraseña, driver):
    try:
        driver.get('http://crm.utel.edu.mx/index.php?module=Users&action=Login')
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value='//*[@id="user_name"]').send_keys(usuario)
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value='//*[@id="user_password"]').send_keys(contraseña)
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value='//*[@id="login_button"]').click()
    except NoSuchElementException:
        credenciales(usuario, contraseña, driver)


def buscar_prospecto(id_crm, driver):
    driver.get("http://crm.utel.edu.mx/index.php?action=ajaxui#ajaxUILoc=index.php%3Faction%3DDetailView%26module%3DLeads%26record%3D"+id_crm)


def dar_click_selector_name(driver):
    driver.find_element(by=By.XPATH, value='// *[ @ id = "list_subpanel_activities"] / table / tbody / tr[1] / td / table / tbody / tr / td[1] / ul / li / span').click()
    driver.find_element(by=By.XPATH, value='// *[ @ id = "Activities_registrarllamada_button"]').click()


def seguimiento(driver, descripcion):
    from datetime import datetime, timedelta
    #atributos
    #primer contacto
    dia_seguimiento = date_now_more_5_days = (datetime.now() + timedelta(days=4)).strftime('%d/%m/%Y')
    asunto_primer_contacto = "PRIMER CONTACTO"
    asunto_seguimiento = "EN SEGUIMIENTO"
    driver.implicitly_wait(10)
    dar_click_selector_name(driver)
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//*[@id="name"]').send_keys(asunto_primer_contacto)
    driver.find_element(by=By.XPATH, value='//*[@id="direction"]/option[2]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="status"]/option[2]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="categoria_c"]/option[3]').click()
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//*[@id="subcategoria_c"]/option[2]').click()
    # guardar
    driver.find_element(by=By.XPATH, value='//*[@id="Calls_subpanel_save_button"]').click()

    #seguimiento
    driver.implicitly_wait(10)
    dar_click_selector_name(driver)
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//*[@id="name"]')().send_keys(asunto_seguimiento)
    driver.find_element(by=By.XPATH, value='//*[@id="direction"]/option[2]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="status"]/option[1]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="date_start_date"]').clear()
    driver.find_element(by=By.XPATH, value='//*[@id="date_start_date"]').send_keys(dia_seguimiento)
    driver.find_element(by=By.XPATH, value='//*[@id="categoria_c"]/option[5]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="subcategoria_c"]/option[6]').click()
    # 2015 - Descripcion
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[1]/ul/li[1]/div[2]/form/div/div[1]/div[1]/div/table/tbody/tr[5]/td[2]/textarea')\
        .send_keys(descripcion)
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//*[@id="Calls_subpanel_save_button"]').click()


def modificar_prospecto(driver, descripcion):
    # editar
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='// *[ @ id = "edit_button"]').click()

    #Apellido .send_keys
    driver.find_element(by=By.XPATH, value='// *[ @ id = "last_name"]').send_keys("S")

    #Carrera .click
    #driver.find_element(by=By.XPATH, value=xpath)('// *[ @ id = "carrera_c"] / option[2]').click()

    #ultimo grado de estudio .click
    driver.find_element(by=By.XPATH, value='// *[ @ id = "plan_estudio_c"] / option[2]').click()

    #Boton de nombre .click
    driver.find_element(by=By.XPATH, value='//*[@id="btn_assigned_user_name"]').click()
    driver.implicitly_wait(10)
    driver.switch_to.window(driver.window_handles[1])

    #nombre popup .send_keys
    driver.find_element(by=By.XPATH, value='//*[@id="first_name_advanced"]').send_keys("Diego")

    #Apellido popup .send_keys
    driver.find_element(by=By.XPATH, value='//*[@id="last_name_advanced"]').send_keys("Bejar")

    #Boton buscar .click
    driver.find_element(by=By.XPATH, value='// *[ @ id = "search_form_submit"]').click()
    driver.implicitly_wait(10)

    #escoger nombre .click

    driver.find_element(by=By.XPATH, value='/html/body/table[4]/tbody/tr[3]/td[2]/a').click()
    driver.implicitly_wait(10)
    driver.switch_to.window(driver.window_handles[0])

    #procedencia .click
    driver.find_element(by=By.XPATH, value='//*[@id="toma_cont_2_c"]/option[15]').click()

    #estado .click
    driver.find_element(by=By.XPATH, value='// *[ @ id = "status"] / option[2]').click()

    #2015 - en seguimiento
    driver.find_element(by=By.XPATH, value='// *[ @ id = "clasif_15_c"] / option[4]').click()

    # 2015 - Descripcion
    driver.find_element(by=By.XPATH, value='// *[ @ id = "description"]').send_keys(descripcion)

    #guardar
    #driver.find_element(by=By.XPATH, value=xpath)('//*[@id="SAVE_FOOTER"]').click()

def buscar_correo(correo, driver):


    #buscar correo y validamos que este o no en la ventana esperada
    urlCorreos = 'http://crm.utel.edu.mx/index.php?module=Leads&action=index'
    isPresent = driver.current_url == urlCorreos
    if (isPresent):
        print()
        llenarInputCorreo(correo, driver)
    else:
        driver.get(
            'http://crm.utel.edu.mx/index.php?module=Leads&action=index')
        llenarInputCorreo(correo, driver)


def llenarInputCorreo(correo, driver):
    from selenium.webdriver.support.ui import WebDriverWait

    WebDriverWait(driver,timeout=10).until(lambda d: d.find_element(by=By.XPATH,value='/html/body/div[2]/div[1]/table/tbody/tr/td/div[3]/form[1]/div[2]/table/tbody/tr[1]/td[4]/input'))
    driver.find_element(by=By.XPATH,
                        value='/html/body/div[2]/div[1]/table/tbody/tr/td/div[3]/form[1]/div[2]/table/tbody/tr[1]/td[4]/input').click()
    driver.find_element(by=By.XPATH,
                        value='/html/body/div[2]/div[1]/table/tbody/tr/td/div[3]/form[1]/div[2]/table/tbody/tr[1]/td[4]/input').clear()
    driver.find_element(by=By.XPATH,
                        value='/html/body/div[2]/div[1]/table/tbody/tr/td/div[3]/form[1]/div[2]/table/tbody/tr[1]/td[4]/input').send_keys(
        correo)
    driver.implicitly_wait(2)
    driver.find_element(by=By.XPATH, value='// *[ @ id = "search_form_submit_advanced"]').click()




def driver():
    #drive chrome
    service = Service(executable_path="webdriver/chromedriver.exe")
    driver = webdriver.WebDriver(service=service)
    driver.implicitly_wait(20)
    #abrir pagina
    return driver



def iniciar(usuario, contraseña, driver):
    try:
        # Automatizar logeo
        credenciales(usuario, contraseña, driver)
        menu(driver)

    except ElementNotVisibleException as e:
        print(Fore.RED + "Te has deslogeado o el elemento ya no existe")
        print(Fore.RED + "El programa se reiniciara")
        iniciar(driver, usuario, contraseña)

    except NoSuchElementException as e:
        print(Fore.RED + "Te has deslogeado o el elemento ya no existe")
        iniciar(driver, usuario, contraseña)


def menu(driver):
    id_crm= ""
    print()
    print(Fore.GREEN + "****************************************")
    print(Fore.GREEN + "********Bienvenido a task-UTEL**********")
    print(Fore.GREEN + "****************************************")
    print()
    print(Fore.GREEN + "Hola Soy Electron. Te voy ayudar a automatizar tus tareas de tipificacion, \n"
          "busqueda de prospectos vía idCrm \n"
          "y tambien busqueda de registros via correo\n"
          "todo esto mientras tu sigues llamando!")
    print()
    while (True):
        try:
            id_crm = input("Ingresa el id_crm a buscar: ").strip()
            buscar_prospecto(id_crm,driver)
            driver.implicitly_wait(10)
            nombre_prospecto = driver.find_element(by=By.XPATH, value='//*[@id="first_name"]').text

            if len(nombre_prospecto)==0:
                print(Fore.RED + "El idm_crm es erroneo o no le pertenece a ningun prospecto")
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
                        automatizar_tarea = ""
                    elif (automatizar_tarea == 2):
                        descripcion = input("Que descripcion quieres poner?")
                        seguimiento(driver, descripcion)
                        automatizar_tarea = ""
                    elif (automatizar_tarea == 3):
                        continue
                    elif (automatizar_tarea == 4):
                        correo_input = input("Ingresa el correo a buscar: ")
                        print()
                        print(Fore.GREEN + "Consejo: Valida los registros y tipifica todos si es que es un seguimiento! \n"
                              "todavia no esta soportado la tipificacion de varios registros en diferentes pestañas!")
                        correo = correo_input.strip()
                        buscar_correo(correo, driver)
                        automatizar_tarea=""

                    elif automatizar_tarea==5:
                        time.sleep(3)
                        print(Fore.RED + "****************************************")
                        print(Fore.RED + "*************Hasta luego****************")
                        print(Fore.RED + "****************************************")
                        print()
                        print(Fore.RED + "**************Task-UTEL ha sido desarrollado por Anarkopin*************")
                        quit()
                        print(Fore.GREEN + "Para ver mas proyectos como este, visita: https://github.com/anarkopin?tab=repositories")
                        print(Fore.GREEN + "Contactame: diebejardelaguila@gmail.com")
                        print()
                        print(Fore.GREEN + "Anarkopin &copy; 2022")
                        quit()
                    else:
                        print(Fore.RED + "No existe tarea o todavia no haz colocado el id_crm")

        except ValueError:
            print(Fore.RED + "Escoge el numero correcto")

        except ElementNotVisibleException as e:
            print(Fore.RED + "Te has deslogeado o no se encontro id_crm o correo")
            print(Fore.RED + "El programa se reiniciara")
            credenciales(usuario,contraseña,driver)
            continue

        except NoSuchElementException as e:
            print(Fore.RED + "Te has deslogeado o no se encontro id_crm o correo")
            print(Fore.RED + "El programa se reiniciara")
            credenciales(usuario,contraseña,driver)
            continue




#DATOS LOGEO


if __name__ == "__main__":
    import sys


    init()
    arg = sys.argv
    archivo=open("contraseña.txt", "r")

    datos = archivo.readlines()
    usuario = datos[0]
    contraseña = datos[1]



    driver = driver()

    iniciar(usuario, contraseña, driver)













