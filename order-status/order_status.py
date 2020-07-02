try:
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys
  from time import sleep
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  driver = webdriver.Chrome(chrome_options=options, executable_path='J:\\Desenvolvimento\\webscraping\\order-status\\chromedriver.exe')
except Exception as error:
  print(f'{error}\nError in a importation!')
except KeyboardInterrupt:
  print('Proccess interrupted by user!')

  
def get_url(url):
  try:
    driver.get(url)
    print('Site is up!')
  except Exception as error:
    print(f'{error}! Program finished!')
  except KeyboardInterrupt:
    print('Proccess interrupted by user!')


def get_status(number_order):
  try:
    get_url('https://www2.correios.com.br/sistemas/rastreamento/default.cfm')
    print('Processing...')
    sleep(2)
    try:
      if driver.find_element_by_class_name('//*[@id="infoMensagem"]/div'):
        print('Please, insert a order number correct!')
        get_status(number_order)
      else:
        fieldset_order = driver.find_element_by_tag_name('fieldset')
        sleep(2)
        fieldset_order.find_element_by_id('objetos').send_keys(number_order)
        sleep(2)
    except Exception as error:
      print(f'{error}')
  except Exception as error:
    print(f'{error}')
  except KeyboardInterrupt:
    print('Proccess interrupted by user!')

def show_infos_status():
  try:
    print('Getting information from order status...', '\n')
    infos_status = driver.find_elements_by_class_name('listEvent')
    sleep(2)
    try:
      for infos in infos_status:
        print(infos.text, '\n')
    except Exception as error:
      print(f'{error}')
    except KeyboardInterrupt:
      print('Proccess interrupted by user!')
      exit()
  except Exception as error:
    print(f'{error}')
  except KeyboardInterrupt:
    print('Proccess interrupted by user!')
    exit()  

def run_script():
  try:
    get_status(order_number)
    sleep(2)
    try:
      print('Processing...')
      fieldset_order = driver.find_element_by_tag_name('fieldset')
      sleep(2)
      search_button = fieldset_order.find_element_by_id('btnPesq')
      sleep(2)
      search_button.submit()
      sleep(5)
      print('')
      show_infos_status()
      driver.quit()
    except Exception as error:
      print(f'{error}')
    except KeyboardInterrupt:
      print('Proccess interrupted by user!')
      exit()
  except Exception as error:
    print(f'{error}')
  except KeyboardInterrupt:
    print('Proccess interrupted by user!')
    exit()

try:
  order_number = input('Order number: ')
  run_script()
  #PY547222295BR
except Exception as error:
  print(error)
except KeyboardInterrupt:
  print('Proccess interrupted by user!')
  exit()