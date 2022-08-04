import configparser
from urllib.parse import unquote

from flask import Flask

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
app = Flask(__name__)

global case
global config
global chrome


def get_chrome():

    global case
    global config
    global chrome
    case = 0

    config = configparser.ConfigParser()
    config.read('../config/config.properties')

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    options = Options()
    #options.add_argument("--disable-notifications")
    #options.add_argument('--headless')
    #options.add_argument("--window-size=1920,1080")
    #options.add_argument(r"user-data-dir=" + "/home/seluser/wpp")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent={0}'.format(user_agent))
    #options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

    chrome = webdriver.Remote(command_executor='http://'+config["settings"]["selenium_host"]+'/wd/hub', options=options)
    chrome.maximize_window()
    #Chrome('./chromedriver_linux', chrome_options=options)

#    chrome.get("https://web.whatsapp.com/")

    return chrome

def get_chrome_connection():

    global chrome

    try:
        chrome.get("https://www.baidu.com/")
    except:
        chrome=get_chrome()

    return chrome


@app.route('/login')
def main():

    global case
    global config
    global chrome
    case = 0

    chrome=get_chrome_connection()
    chrome.get("https://web.whatsapp.com/")

    return "succes"


@app.route('/login_hp')
def login_hp():
    global chrome
    #time.sleep(3)
    #chrome.save_screenshot('whatsapp.png')
    #time.sleep(32)
    #os.unlink('wdocker hatsapp.png')
    chrome=get_chrome_connection()
    chrome.get("https://www.helperplace.com/")
    time.sleep(4)
    #chrome.save_screenshot('whatsapp.png')

    login = chrome.find_element(By.XPATH, '//*[@id="togglebtn"]/ul/li[7]/a')
    login.click()

    time.sleep(2)

    email = chrome.find_element(By.XPATH, '//*[@id="pills-home"]/div/div[1]/input')
    email.send_keys("patrickkwanpccw@gmail.com")

    password = chrome.find_element(By.XPATH, '//*[@id="pills-home"]/div/div[2]/input')
    password.send_keys("patrick@pccw")

    button = chrome.find_element(By.XPATH, '//*[@id="pills-home"]/div/div[5]/button')
    button.click()

    app.logger.info("HP login success!")

    return "hp success"
    #chrome.get('https://www.helperplace.com/candidate-shortlist/all?page=1')
    #filter(chrome)
    #time.sleep(5)
    #numOfPage = int(pageLinks[len(pageLinks) - 2].text)
    #go_page(chrome, 1)


@app.route("/send/<location>/<position>/<name>/<id>")
def handle_helper_link(location,position,name,id):

    global chrome
    app.logger.info(location)
    app.logger.info(position)
    app.logger.info(name)
    app.logger.info(id)

    prefix="https://www.helperplace.com/resume/"
#    prefix = "https://www.helperplace.com/resume/hong-kong/domestic-helper/"
#    name='String => {}'.format(name)
#    id='String => {}'.format(id)

    helperLink=prefix+location+"/"+position+"/"+name+"/"+id
    app.logger.info(helperLink)

    app.logger.info("\nclicking into helper detail")
    chrome=get_chrome_connection()
    chrome.get(helperLink)

    contactBtn = WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@title='Contact Candidate']")))
    try:
        chrome.find_element(By.CLASS_NAME, "custom-expire-banner").size
        app.logger.info("EXPIRED!!!!")
        return "EXPIRED"
    except:
        app.logger.info("not expired")
    contactBtn.click()

    calltab = WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.XPATH, "// *[@id='calling-tab']")))
    calltab.click()

    callbtn = WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "calling-btn")))
    mobile = WebDriverWait(callbtn, 10).until(
        EC.element_to_be_clickable((By.XPATH, "li/a/span"))).text.replace("=","").replace("-","")

    #mobile = chrome.find_element(By.CLASS_NAME, "calling-btn").find_element(By.XPATH, "li/a/span").text.replace("=","").replace("-","")
    app.logger.info("mobile="+mobile)
    helpername = chrome.find_element(By.CLASS_NAME, "listing-about-title").text.split("(")[0]

    subtitle = chrome.find_element(By.CLASS_NAME, 'listing-about-sub-title').text
    numofexp = chrome.find_element(By.XPATH,"/html/body/section/app-root/app-resumeview/section/section[2]/div/div/div[1]/div/div/div/div/div[3]/div/div[2]/div[1]/h3").text
    numofexp = numofexp.split(" ")[0]
    if subtitle.find("Filipino") > -1:
        nationality = "Filipino"
    elif subtitle.find("Indonesian") > -1:
        nationality = "Indonesian"
    else:
        nationality = "etc"
    app.logger.info("helpername="+helpername)
    app.logger.info("nationality="+nationality)
    app.logger.info("numofexp="+numofexp)
    result=whatsapp(mobile, helpername,nationality,numofexp)
    return result


def whatsapp(mobile,helpername,nationality,numofexp):
    try:
        chrome.get("https://web.whatsapp.com/send/?phone="+mobile)
        #time.sleep(22)
        send_wa_msg("Hi "+helpername+". My name is Camy")
        send_wa_msg("I am an employment agency")
        send_wa_msg("I would like to find a "+nationality+" helper with "+numofexp+" years experience")
        send_wa_msg("Are you still looking for job?")
    except:
        app.logger.info("wrong in whatsapp")
        return "FAIL"

    app.logger.info("Msg Sent!")
    return mobile

@app.route("/sendwa/<mobile>/<msg>")
def whatsapp2(mobile,msg):

    global chrome

    msg=unquote(msg)
    print("msg=" + msg)
    msgs = msg.split("<<<<<<")
    print(msgs)

    try:
        chrome=get_chrome_connection()
        chrome.get("https://web.whatsapp.com/send/?phone="+mobile)

        for _msg in msgs:
            __msgs = _msg.split(">>>>>>")
            for i in range(len(__msgs)):
                msgbox = WebDriverWait(chrome, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@title = "Type a message"]/p')))
                msgbox.send_keys(__msgs[i])
                if i<len(__msgs)-1:
                    ActionChains(chrome).key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
            #wa_send_btn = WebDriverWait(chrome, 10).until(
        #    EC.element_to_be_clickable((By.XPATH, '//*[@data-testid = "send"]/..')))
        #wa_send_btn.click()
    except:
        app.logger.info("wrong in whatsapp")
        return "FAIL"

    print("Msg Sent!")
    app.logger.info("Msg Sent!")
    return "SUCCESS"


def send_wa_msg(msg):

    global chrome

    msgbox = WebDriverWait(chrome, 120).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@title = "Type a message"]/p')))
    msgbox.send_keys(msg)
    wa_send_btn = WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@data-testid = "send"]/..')))
    #chrome.find_element(By.XPATH, '//*[@title = "Type a message"]/p').send_keys(msg)
    wa_send_btn.click()


#if __name__ == '__main__':
#    app.run('0.0.0.0', 5000, debug=True)