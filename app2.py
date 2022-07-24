import datetime
import os
import pathlib
from typing import Any

import configparser
import sqlite3
import sys

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
#from PIL import Image
#from Screenshot import Screenshot_clipping
#from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.by import By

test = True
global case
global config
global chrome

def main():

    global case
    global config
    global chrome
    case = 0

    config = configparser.ConfigParser()
    config.read('config/config.properties')

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    options = Options()
    #options.add_argument("--disable-notifications")
    #options.add_argument('--headless')
    #options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent={0}'.format(user_agent))
    #options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

    chrome = webdriver.Remote(command_executor='http://20.205.106.141:4445/wd/hub', options=options)
    chrome.maximize_window()
    #Chrome('./chromedriver_linux', chrome_options=options)



    chrome.get("https://web.whatsapp.com/")
    time.sleep(3)
    #chrome.save_screenshot('whatsapp.png')
    time.sleep(32)


def go_chrome(chrome, page):

    global config
    page = page - 1
    #print('https://www.helperplace.com/candidate-shortlist/all?country=Hong-Kong,Indonesia,Philippines&job_position=Domestic-Helper&nationality=Indonesian&contract_status=Finished-Contract&post_manager=Direct&Language=Cantonese&page=' + str(page + 1))
    #chrome.get('https://www.helperplace.com/candidate-shortlist/all?country=Hong-Kong,Indonesia,Philippines&job_position=Domestic-Helper&nationality=Indonesian&contract_status=Finished-Contract&post_manager=Direct&Language=Cantonese&page=' + str(page + 1))
    chrome.get(
        'https://www.helperplace.com/candidate-shortlist/all?'
        'country='+config["settings"]["country"]+'&'
        'job_position=Domestic-Helper&'
        'nationality='+config["settings"]["nationality"]+'&'
        'post_manager=Direct&'
        'Language='+config["settings"]["Language"]+'&page='
        + str(page + 1))
    time.sleep(5)


def go_page(chrome, page):
    go_chrome(chrome, page)
    pagination = chrome.find_element(By.CLASS_NAME, 'pagination').find_elements(By.XPATH, 'li')
    numOfPage = pagination[len(pagination) - 2].text
#        print("numOfPage=" + numOfPage)
    print("\n\nBrowsing page " + str(page)+" of "+str(numOfPage)+"\n\n")

    helpers = chrome.find_element(By.CLASS_NAME, "container-fluid").find_elements(By.XPATH, "div/div")
    #By.XPATH,
    #                               '/html/body/section/app-root/app-candidate-shortlist/section/div/div[4]/div[2]/div/div/div[3]/div/div[1]/div/div/div')

    for helperNum in range(len(helpers)):

        if helperNum != 5:
            print("\nListing in page " + str(page) + " of " +numOfPage+ ", helperNum="+str(helperNum) + " of " + str(len(helpers)))
            try:
                helperElement= chrome.find_element(By.CLASS_NAME, "container-fluid").find_elements(By.XPATH, "div/div")[helperNum]
            except:
                wait_for_time(chrome)
                go_page(chrome, 1)

            #'<div _ngcontent-serverapp-c136="" class="row ng-star-inserted"><!----><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/mila/55921"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Mila" src="https://cdn.helperplace.com/cpi/55921_1655420406.jpg"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/mila/55921"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Mila <span _ngcontent-serverapp-c109="">- 36<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Break Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> Dear employer, I am Mila, 36 years old, Single. I'm from Indonesia. I have been working as a Domestic Helper for 15 years. My current employers are 1 elderly adult. I have worked with them for 3 months. My duties are housekeeping, cooking, and market... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>14yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 08 Aug 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/rustiani/30285"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Rustiani " src="https://cdn.helperplace.com/cpi/30285_1648520207.jpg"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/rustiani/30285"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Rustiani  <span _ngcontent-serverapp-c109="">- 48<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Break Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> I am Rustiani, 48 years old, Widowed with 1 kid. I'm from Indonesia. I have been working as a Domestic Helper for 5 years and 8 months - 2 years in Malaysia and 3 years and 8 months in Hong Kong. I just started with my current employers are 2 adults.... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>12yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 30 Sep 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/adriana-septi/49402"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Adriana septi" src="https://cdn.helperplace.com/cpi/49402_1656741699.jpg"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/adriana-septi/49402"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Adriana septi <span _ngcontent-serverapp-c109="">- 35<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> My name is Adriana, 35 years old, with 1 child, I'm from Indonesia,I've been working as a domestic helper for 13 years,6 years in Singapore n 7 years in Hong Kong. I am for 2 years with my current employer, they are one adult with elderly ( 90 years ... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>14yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 31 Aug 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: rgb(235, 186, 22);"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/fenny/58042"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Fenny " src="https://cdn.helperplace.com/cpi/58042_1656732919.JPG"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/fenny/58042"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Fenny  <span _ngcontent-serverapp-c109="">- 26<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> Hi, my name is Fenny. I am Indonesian and&nbsp;Single. I am 26 years old and currently here in Hong Kong.&nbsp;I&nbsp;take care of a newborn baby till now he was 4 years old soon. I do all at the household chores.&nbsp; I am now looking for a new employer and hope you c... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>4yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 18 Oct 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/anggun/50597"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="ANGGUN " src="https://cdn.helperplace.com/cpi/50597_1652401450.JPG"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/anggun/50597"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> ANGGUN  <span _ngcontent-serverapp-c109="">- 39<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> Hello ma’am and sir, I’m Anggun or you may call me wati for making it easier for you to call me. I’m Indonesian and I’m 39 years old. I’m a single mother of one daughter and she is now 20 years old and still learning in the University in my hometown ... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>14yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 07 Oct 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><!----><div _ngcontent-serverapp-c109="" class="mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box advertise-container"><a _ngcontent-serverapp-c109="" rel="nofollow"><img _ngcontent-serverapp-c109="" class="adv_banner_img img-fluid adv_banner_web" src="https://cdn.helperplace.com/adv_w/40_1604567909.webp" alt="https://cdn.helperplace.com/adv_w/40_1604567909.webp"><img _ngcontent-serverapp-c109="" class="adv_banner_img img-fluid adv_banner_mobile" src="https://cdn.helperplace.com/adv_m/40_1604567907.webp" alt="https://cdn.helperplace.com/adv_m/40_1604567907.webp"><span _ngcontent-serverapp-c109="" class="d-none">Ads by Helperplace</span></a></div></div><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/driver/muhamad/53407"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Muhamad " src="https://cdn.helperplace.com/cpi/53407_1655442186.jpg"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/driver/muhamad/53407"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Muhamad  <span _ngcontent-serverapp-c109="">- 39<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Driver </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> I'm Muhammad Ali, you can call Ali, I'm 39 years old, I'm not married yet, but I'm already engaged, I worked in Hong Kong almost 10 years, my first employer 2012~2014 I worked take care of Disable grandfather in Shatin but I didn't finish the contrac... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>2yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 06 Sep 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/rosy/14733"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Rosyieda" src="https://cdn.helperplace.com/cpi/14733_1619831389.JPG"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/rosy/14733"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Rosyieda <span _ngcontent-serverapp-c109="">- 32<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> My name is Rosyieda, I’m 32 years old, singe parent with 1 child. I’m from Indonesia. I’ve been working as a domestic helper for 7 years here in Hong Kong. My contract will end at November 2022with my current employer, they are 3 elderly (98, 97 and ... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>7yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 20 Nov 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/seti/54649"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Seti " src="https://cdn.helperplace.com/cpi/54649_1654703143.JPG"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/seti/54649"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Seti  <span _ngcontent-serverapp-c109="">- 39<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> I am Seti, 39 years old, Single. I'm from Indonesia. I have been working as a Domestic Helper for 16 years - 4 years in Singapore, and 12 years in Hong Kong. My current employers are 3 elderly adults. I have worked with them for 4 years. My duties ar... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>12yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 28 Sep 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/very/53433"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Very" src="https://cdn.helperplace.com/cpi/53433_1656949177.jpg"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/very/53433"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Very <span _ngcontent-serverapp-c109="">- 30<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> I am Very, 30 years old, Married with 1 kid. I'm from Indonesia. I have been working as a Domestic Helper for 6 years - 4 years in Singapore, and 2 years in Hong Kong. My current employers are 4 adults and 1 kid (4 years old). I have worked with them... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>6yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 19 Nov 2022 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/mariati/59536"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Mariati" src="https://cdn.helperplace.com/cpi/59536_1657526972.jpg"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/mariati/59536"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Mariati <span _ngcontent-serverapp-c109="">- 60<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> I've been&nbsp;working for 12 years taking care of elderly in one employer for that long. I am a good to take care of elderly. I can cook do household works, marketing. I am physically fit and I am still strong to take care and do my job.... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>12yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 01 Feb 2023 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/triyani/58847"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Triyani " src="https://cdn.helperplace.com/cpi/58847_1657269568.jpg"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/triyani/58847"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Triyani  <span _ngcontent-serverapp-c109="">- 36<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Finished Contract </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> Hi, my name is Triyani, from Indonesia, I did work with same employer for 5 years and will end contract on march 2023. I am&nbsp;taking&nbsp;care of two kids, cleaning, cooking, buy groceries, send them classes and drop them school and pick up them to, i can c... </div><div _ngcontent-serverapp-c109="" class="product-footer"><h5 _ngcontent-serverapp-c109="" class="footer-experience"><i _ngcontent-serverapp-c109="" class="fa fa-certificate"></i>5yr experience </h5><h5 _ngcontent-serverapp-c109="" class="footer-date ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-calendar"></i>From 01 Feb 2023 | Full Time </h5><!----><h5 _ngcontent-serverapp-c109="" class="footer-active ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-circle"></i>Very Active </h5><!----></div></a></div></div><div _ngcontent-serverapp-c109="" class="row bg-primary py-2 w-100 positions m-0 px-1 inherit-bottom ng-star-inserted"><div _ngcontent-serverapp-c109="" class="col-12 px-1 text-left"><a _ngcontent-serverapp-c109="" class="custom-save-job ng-star-inserted"><!----><i _ngcontent-serverapp-c109="" class="fa fa-bookmark mr-1 ng-star-inserted" style="color: white;"></i><!----> Shortlist Candidate </a><!----><!----><!----><!----></div></div><!----></div><!----><!----><!----><!----></candidate-detail-block></div><div _ngcontent-serverapp-c136="" class="col-12 col-12_padding_Set ng-star-inserted"><!----><candidate-detail-block _ngcontent-serverapp-c136="" _nghost-serverapp-c109=""><div _ngcontent-serverapp-c109="" class="product-box-container mb-4 ng-star-inserted"><div _ngcontent-serverapp-c109="" class="product-box"><div _ngcontent-serverapp-c109="" class="img-wrapper_Custom w-10"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/indra/21724"><div _ngcontent-serverapp-c109="" class="front custom_front_rsume_image"><img _ngcontent-serverapp-c109="" loading="lazy" onerror="this.src='assets/images/images.png'" alt="Indra" src="https://cdn.helperplace.com/cpi/21724_1625794511.jpg"><span _ngcontent-serverapp-c109="" class="d-none">Helper Profile Image</span></div></a><div _ngcontent-serverapp-c109="" class="listing-sub-title-agency text-left w-20 mt-2"><label _ngcontent-serverapp-c109="" for="lable_type" class="label_blue"><!----><span _ngcontent-serverapp-c109="" class="ng-star-inserted">Direct</span><!----></label></div></div><div _ngcontent-serverapp-c109="" class="product-detail w-100 pt-2 align-self-baseline text-left"><a _ngcontent-serverapp-c109="" routerlinkactive="router-link-active" href="/resume/hong-kong/domestic-helper/indra/21724"><!----><!----><h4 _ngcontent-serverapp-c109="" class="product-title"> Indra <span _ngcontent-serverapp-c109="">- 39<label _ngcontent-serverapp-c109="">yr</label></span></h4><div _ngcontent-serverapp-c109="" class="product-header-description"><h5 _ngcontent-serverapp-c109="" class="product-sub-title 1 mt-1"><span _ngcontent-serverapp-c109="">Domestic Helper </span>- Terminated (Other) </h5><h5 _ngcontent-serverapp-c109="" class="product-location ng-star-inserted"><i _ngcontent-serverapp-c109="" aria-hidden="true" class="fa fa-map-marker dark"></i>Hong Kong </h5><!----></div><div _ngcontent-serverapp-c109="" class="product-description mt-2" style="word-break: break-word;"> My name Indra. I am 39 years old. I work&nbsp;in Hong Kong&nbsp;for 10 years:

            try:
                name = helperElement.find_element(By.CLASS_NAME, "product-title").text
            except:
                wait_for_time(chrome)
                go_page(chrome, 1)
            try:
                contractText = helperElement.find_element(By.CLASS_NAME, "product-sub-title").text
            except:
                wait_for_time(chrome)
                go_page(chrome, 1)
            try:
                contacted = helperElement.find_element(By.CLASS_NAME, "contacted-chip").text
            except:
                contacted = "No Contact"
                                                          # ""'candidate-detail-block/div/div[1]/div[2]/a/div[1]').text
            direct = helperElement.find_element(By.XPATH, 'candidate-detail-block/div/div[1]/div[1]/div/label/span').text
            helperLink = helperElement.find_element(By.XPATH, 'candidate-detail-block/div/div[1]/div[2]/a').get_attribute("href")

            con = sqlite3.connect('autohelperplace.db')
            cursorObj = con.cursor()
            cursorObj.execute("SELECT * FROM helperlinks where link='" + helperLink + "'")
            rows = len(cursorObj.fetchall())
            con.close()

            print("name="+name)
            print("contractText="+contractText)
            print("contacted="+contacted)
            print("direct="+direct)
            print("rows="+str(rows))

            if rows > 0:
                print("\n******** Contacted! DB found ********\n")
            elif direct.find("Direct") == -1:
                print("\n******** Skip for Agent! ********\n")
            elif contractText.find("Break") > -1:
                print("\n******** Skip for contract break! ********\n")
            elif contacted.find("Contacted") > -1:
                print("\n******** Contacted! ********\n")
            else:
                print("Not Contacted!")

                handle_helper_link(chrome, helperLink, page)

                go_page(chrome, page)
            time.sleep(1)
    #find next page
    try:
        go_page(chrome, page+1)
    except:
        wait_for_time(chrome)
        go_page(chrome, 1)


def handle_helper_link(chrome, helperLink, page):

    print("\nclicking into helper detail")

    con = sqlite3.connect('autohelperplace.db')
    cursorObj = con.cursor()

    chrome.get(helperLink)
    time.sleep(5)
    name = chrome.find_element(By.CLASS_NAME, "product-detail").find_element(By.XPATH, "h1").text.split(" ")[0]
    subtitle = chrome.find_element(By.CLASS_NAME, 'listing-about-sub-title').text
    position = chrome.find_element(By.CLASS_NAME, 'footer-experience').find_element(By.XPATH, "i").text
    #contract = chrome.find_element(By.CLASS_NAME, 'footer-experience').find_element(By.XPATH, "i").text.split("|")[1]
    #numofexp = chrome.find_element(By.XPATH,
    #                               '/html/body/section/app-root/app-resumeview/section/section[2]/div/div[2]/div[1]/div/div/div/div/div[3]/div/div[2]/div[1]/h3').text
    salaryText = chrome.find_element(By.XPATH, "//*[contains(text(),'Salary:')]")

    if subtitle.find("Filipino") > -1:
        nationality = "Filipino"
    elif subtitle.find("Indonesian") > -1:
        nationality = "Indonesian"
    else:
        nationality = "etc"

    try:
        salary = salaryText.find_element(By.XPATH, '../h3[2]').text
    except NoSuchElementException:
        salary = salaryText.find_element(By.XPATH, '../h3[2]/span').text
    try:
        salary = int(salary.split("HK$")[1].replace("(≈", "").replace(")", "").replace(",", "").strip())
    except:
        salary = 10000
    print("name="+name)
    print("nationality="+nationality)
    print("salary="+str(salary))

    if salary > 6000:
        print("\n******** Skip for high salary! ********\n")
        #cursorObj.execute("CREATE TABLE IF NOT EXISTS helperlinks (link text NOT NULL PRIMARY KEY)")
        cursorObj.execute("INSERT INTO helperlinks VALUES('" + helperLink + "', TIME(),'SALARY_HIGH')")
        con.commit()

    else:
        contactBtn = chrome.find_element(By.XPATH, "//*[@title='Contact Candidate']")
        contactBtn.click()
        time.sleep(1)
        calltab = chrome.find_element(By.XPATH, '// *[@id="calling-tab"]')
        calltab.click()
        time.sleep(1)
        mobile = chrome.find_element(By.CLASS_NAME, "calling-btn").find_element(By.XPATH, "li/a/span").text.replace("=","").replace("-","")
        print("mobile="+mobile)
        try:
            chrome.get("https://web.whatsapp.com/send/?phone="+mobile+"&text&type=phone_number&app_absent=0")
            time.sleep(22)
            chrome.find_element(By.XPATH, '//*[@title = "Type a message"]/p').send_keys("Hi "+name+ ". Are you looking for job?")
            time.sleep(2)
            chrome.find_element(By.XPATH, '//*[@data-testid = "send"]/..').click()

            cursorObj.execute("INSERT INTO helperlinks VALUES('" + helperLink + "', TIME(),'SUCCESS')")
            con.commit()
            time.sleep(5)


        except:
            print("wrong in whatsapp")
            cursorObj.execute("CREATE TABLE IF NOT EXISTS helperlinks (link text NOT NULL PRIMARY KEY)")
            cursorObj.execute("INSERT INTO helperlinks VALUES('" + helperLink + "', TIME(),'WRONG_WHATSAPP')")
            con.commit()

        #msg = 'Hello ' + name + '!\nAre you looking for job?\nI have some Ma\'am is finding a ' + nationality + ' ' + position + '.\nThey are very interested to your profile.\n\nTo better present you to Ma\'am, I want you to fill up the form to let Ma\'am know you more.'
        #msg += 'Or you may whatsapp me, +852 52768846 to discuss if you have more wish'
        #chrome.find_element(By.XPATH, '//*[@id="message"]/div[1]/textarea').send_keys(msg)
        #time.sleep(2)
        #if not test:
        #    contactSendBtn = chrome.find_element(By.XPATH, '// *[ @ id = "message"] / div[4] / button[2]')
        #    contactSendBtn.click()
        print("Msg Sent!")
        global case
        case = case + 1
        print("case="+str(case))
        if case >= int(config["settings"]["count"]):
            wait_for_time(chrome)
        else:
            time.sleep(int(config["settings"]["time_after_msg"]))


def wait_for_time(chrome):
    global case
    global config

    case = 0
    checktime = int(config["settings"]["checktime"])
    checkhour1 = int(config["settings"]["checkhour1"])
    checkhour2 = int(config["settings"]["checkhour2"])
    checkminute = int(config["settings"]["checkminute"])
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    while not ((hour == checkhour1 or hour == checkhour2)
               and minute <= checkminute+checktime and minute >= checkminute-checktime):
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        print("now is " + str(hour) + ":" + str(minute) + "... waiting")
        chrome.get("https://www.google.com")
        time.sleep(checktime*60)
    print("now is " + str(hour) + ":" + str(minute) + "... start again")
main()
