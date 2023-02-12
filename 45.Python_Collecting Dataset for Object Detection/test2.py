from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
import pandas as pd
import os
import time
import urllib.request

# 키워드 가져오기
keyss = pd.read_csv('./keyword.txt', encoding='utf-8', names=['keyword'])
keyword = []
[keyword.append(keyss['keyword'][x]) for x in range(len(keyss))]

print(keyword)

# 이미지 저장할 폴더 구성
def create_folder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError as e:
        print('Error creating folder : ',dir,'\nerror : ', e)

# image download 함수
def image_download(keyword):
    create_folder('./' + keyword + '/')

    # chromedriver 가져오기
    chromedriver = './chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(3)

    print('keyword : '+ keyword)
    driver.get('https://www.google.co.kr/imghp?hl=ko')
    keywords = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    keywords.send_keys(keyword)
    keywords.send_keys(Keys.RETURN)

    print(keyword+' 스크롤 중 .............')
    elem = driver.find_element_by_tag_name("body")

    range_image = 500

    for i in range(range_image):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)

    try:
        driver.find_element_by_xpath(
            '//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input').click()
        for i in range(range_image):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
    except:
        pass

    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    print(keyword+' 찾은 이미지 개수:', len(images))

    links = []
    for i in range(1, len(images)):
        try:
            print('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')

            driver.find_element_by_xpath(
                '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').click()
            links.append(driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src'))
            # driver.find_element_by_xpath('//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a').click()
            print(keyword+' 링크 수집 중..... number :'+str(i)+'/'+str(len(images)))
        except:
            continue

    forbidden = 0
    for k, i in enumerate(links):
        try:
            url = i
            start = time.time()
            urllib.request.urlretrieve(
                url, "./"+keyword+"/"+str(k-forbidden)+".jpg")
            print(str(k+1)+'/'+str(len(links))+' '+keyword +
                  ' 다운로드 중....... Download time : '+str(time.time() - start)[:5]+' 초')
        except:
            forbidden += 1
            continue
    print(keyword+' ---다운로드 완료---')

    driver.close()



# =====================================================================
# 실행
# =====================================================================
if __name__ == '__main__':
    pool = Pool(processes=1) # 프로세스 사용(창 갯수)
    pool.map(image_download, keyword)