import requests
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import time
from django.core.exceptions import ObjectDoesNotExist
import django
import os


class Spider:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def parse(self):
        for i in range(50):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.driver.execute_script("window.scrollTo(0,0)")
            time.sleep(random.randint(3, 6))
        page = self.driver.page_source
        with open('web_fengtai.html', 'w') as f:
            f.write(page)

        # page = open('web2.html', encoding='utf-8').read()
        # doc = pq(page)
        # from meituan.models import Index
        # items = doc('#wm-container div div ul li[data-watch]').items()
        # for item in items:
        #     try:
        #         line = Index.objects.get(shop_id=item.attr('data-watch'))
        #         print('Existed %s' % line)
        #     except ObjectDoesNotExist:
        #         line = Index(shop_id=item.attr('data-watch'),
        #                      name=item.find('a[aria-label]').attr('aria-label'),
        #                      remark=item.text(),
        #                      center='丰台科技园地铁站')
        #         line.save()
        #         print('Insert %s' % line)

    def parse2(self):
        from meituan.models import Shop, Product, Index
        url = 'https://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId=%(shop_id)s&utm_source=&channel=default&source=shoplist&initialLat=40.00366&initialLng=116.326836&actualLat=31.205336&actualLng=121.404163'
        items = Index.objects.filter(id__gt=8)
        for item in items:
            time.sleep(random.randint(2, 6))
            self.driver.get(url % {'shop_id': item.shop_id})
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="scrollArea"]/div[3]/nav/div[3]'))
            )
            try:
                self.driver.find_element_by_xpath('//*[@id="scrollArea"]/div[3]/nav/div[3]').click()
            except:
                continue
            addr_xpath = '//*[@id="scrollArea"]/div[3]/div/div[1]/div[3]/div[1]/div[1]/p'
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, addr_xpath))
            )
            page = self.driver.page_source
            with open('shops/%s.html' % item.shop_id, 'w', encoding='utf-8') as f:
                f.write(page)
            address = self.driver.find_element_by_xpath(
                '//*[@id="scrollArea"]/div[3]/div/div[1]/div[3]/div[1]/div[1]/p').text
            if not Shop.objects.filter(index=item.id).exists():
                shop = Shop(name=item.name, address=address)
                shop.save()
                print('Insert %s' % shop)

    # def run(self):
    #     self.parse()


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'myjobs.settings'
    django.setup()
    s = Spider()
    s.parse()
