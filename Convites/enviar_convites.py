from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = 'C:\\Users\\Administrador\\Desktop\\testechrome\\chromedriver_win32\\chromedriver.exe'


chrome_binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


chrome_service = ChromeService(executable_path=driver_path)


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_location


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


driver.get("https://web.whatsapp.com/")


input("Por favor, faça o login manualmente e pressione Enter quando estiver pronto.")


contatos_alvo = ["Pedro Work", "Victor Spinoza", "Grid"]


mensagem_oi = "Olá Pessoal Sejam bem vindos ao meu aniversario de 30 aninhos, conto com a presença de todos voces.!"


for contato_alvo in contatos_alvo[:3]:
    
    campo_pesquisa = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
    )

    print("Campo de pesquisa encontrado com sucesso.")

   
    campo_pesquisa.send_keys(contato_alvo)

   
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[@title='{contato_alvo}']"))
    ).click()

   
    campo_mensagem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.g0rxnol2 div[data-tab='10']"))
    )


    campo_mensagem.send_keys(mensagem_oi)

    
    campo_mensagem.send_keys(Keys.RETURN)


    driver.implicitly_wait(2)


input("Pressione Enter para fechar o navegador.")


driver.quit()
