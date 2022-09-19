from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from metodos.metodos import *


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
        print("ingresamos al except")
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
    driver.find_element(by=By.XPATH, value='// *[ @ id = "edit_button"]')().click()

    #Apellido .send_keys
    driver.find_element(by=By.XPATH, value='// *[ @ id = "last_name"]')().send_keys("S")

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
    #buscar correo

    element = '// *[ @ id = "email_advanced"]'
    isPresent = len(driver.find_elements(By.XPATH,element)) > 0
    if (isPresent):
        print()
    else:
        driver.get('http://crm.utel.edu.mx/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DLeads%26action%3Dindex%26parentTab%3DMarketing')

    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='// *[ @ id = "email_advanced"]').clear()
    driver.find_element(by=By.XPATH, value='// *[ @ id = "email_advanced"]').send_keys(correo)
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='// *[ @ id = "search_form_submit_advanced"]').click()


