from selenium import webdriver
from selenium.webdriver.support.select import Select
import urllib
import urllib.request
from io import BytesIO
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import json
import time
import sys


a=datetime.now()

date = datetime.today().strftime('%d-%m-%Y')

log = open('C:/Users/Zaakki/Desktop/PhD/MISC Projects/TASI Data/Logs/TASI_Log_%s.txt' % date, 'w')
sys.stdout = log

with open('TASI_Data_%s.json' % date, 'w') as f:
    json.dump([], f)
f.close()

driver = webdriver.Chrome('C:/Web_drivers/Chrome/chromedriver.exe') 
driver.implicitly_wait(90) # this lets webdriver wait 10 seconds for the website to load
driver.maximize_window()
#driver.get("https://www.tadawul.com.sa/wps/portal/tadawul/markets/equities/indices/today/!ut/p/z1/rZJBT8IwFMc_i4cepW8wQb01JsyaSUJkMHtZStdITdcubWH47R3Ei4kWDfTy0rzfr8n_9WGGS8wM36k3HpQ1XPf3VzauhsOH2-QuhRzySQJknAGdP6ejbAp4FQMgSzD7l5_R2QTInDwup8tF74_O8yH9mw-_HAKnfRZFZkkcOI7oO_DDDKLAIeQRiKR4OpWj_-hNCO09AgRd1w3UuhkI2yDYN9p4BK2zNYKaBx4-WolAWBOkCQic9HbrhLwWVmspDnvjMQt8TU0t97j8Kpd9Xmy4C1XgXlVi61xPVr5vWofLBXmhuG2KoihB0fcbvcvJ1ScB2Jx-/p0/IZ7_NHLCH082KGN530A68FC4AN2O63=CZ6_22C81940L0L710A6G0IQM43GF0=MEtabIndex!ListedCompanies=chart_tasi_current_sector!TASI==/")
driver.get("https://www.saudiexchange.sa/wps/portal/tadawul/markets/equities/indices/today/!ut/p/z1/rZJdT8IwFIZ_ixe9lJ7BBPWuMWHWTCKR4ezNUroqM_1YusLw31u4M9GigXPXnOdJ874tZrjEzPBt8859Yw1X4fzKxtVweHed3KSQQz5JgIwzoPPHdJRNAb_EAMgSzP7lZ3Q2ATIn98vpchH80Wk-pH_z4ZchcNxnUWSWxIFDRd-BHzqIAvuQByCS4uFYjvDQa-_bWwQI-r4fNCs9EFYj2GllOgStszWCmnvuP1uJQFjjpfEInOzsxgl5KaxSUuz_TYeZ5ytqarnD5ZN0b9ZpboQ89yVizZ2vPO-aSmycC2TVhaV1uFyQZ4pbXRRFCQ39uFLbnFx8AZWL71c!/p0/IZ7_NHLCH082KGN530A68FC4AN2O63=CZ6_22C81940L0L710A6G0IQM43GF0=MEtabIndex!ListedCompanies=chart_tasi_current_sector!TASI==/?")
constituents =driver.find_element_by_css_selector('#layoutContainers > div > div.row > div.col-xs-14.col-md-11.col-lg-9 > div > div > div > div > div.component-container.wpthemeCol.wpthemeSecondaryContainer.ibmDndColumn.id-Z7_NHLCH082KGN530A68FC4AN2OS7 > div.component-control.id-Z7_NHLCH082KGN530A68FC4AN2OE0')

time.sleep(5)
no_of_pages = driver.find_element_by_css_selector('#table5_paginate > span.paginate_of')
pages = no_of_pages.text 
pages = int(re.search(r'\d+', pages).group()) + 1

print("Total pages : ", pages-1)
print("")

for y in range(1,pages):
        time.sleep(4)

        select = Select(driver.find_element_by_css_selector('#table5_paginate > select'))
        current_page= select.first_selected_option.get_attribute("value")


        if current_page!= y:
            select.select_by_value('{}'.format(y))

        table=driver.find_element_by_css_selector('#table5')
        for tr in table.find_elements_by_tag_name('tr'):
            count = len(table.find_elements_by_tag_name("tr"))
        print("Current page row count : ", count-1)
        print("Currently on page : ", y)
        print("")

        for x in range(1,count):
            time.sleep(3)
            element2 = driver.find_element_by_css_selector('#table5')
            coordinates = element2.location_once_scrolled_into_view
            driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))

            individual_comp =driver.find_element_by_css_selector('#table5 > tbody > tr:nth-child({}) > td:nth-child(2) > a'.format(x))
            individual_comp.send_keys(Keys.RETURN)
            time.sleep(3)
            try:
                reference_num = driver.find_element_by_css_selector('#index_head > p')
            except:
                count-1
                driver.execute_script("window.history.go(-1)")
            
            ref_text = reference_num.text
            #print(ref_text)

            comp_name = driver.find_element_by_css_selector('#index_head > div > h2') 
            comp_text = comp_name.text 
            print("Currently on Company Number : ", x)
            print(comp_text)
            print("")

            trading_name = driver.find_element_by_css_selector('#index_head > div > p:nth-child(2) > strong') 
            trading_text = trading_name.text
            #print(trading_text)

            sector_name = driver.find_element_by_css_selector('#index_head > div > p:nth-child(3) > strong') 
            sector_text = sector_name.text  
            #print(sector_text)

            industry_group = driver.find_element_by_css_selector('#index_head > div > p:nth-child(3) > a')  
            industry_text = industry_group.text 
            #print(industry_text)

            price = driver.find_element_by_xpath('//*[@id="chart_tab1"]/div[1]/div[1]/div[1]/dl/dd').text   
            #print(price)

            change = driver.find_element_by_xpath('//*[@id="chart_tab1"]/div[1]/div[1]/div[2]/dl/dd').text
            change_val = change.split('(')[0]
            change_percent = re.search(r'\((.*?)\)',change).group(1) #change[change.find("(")+1:change.find(")")] #\S
            #print(change_val)
            #print(change_percent)

            previous_close = driver.find_element_by_css_selector('#chart_tab1 > div:nth-child(1) > div:nth-child(2) > div.col-xs-14.col-sm-2.col-md-3.col-lg-3 > dl > dd')   
            prev_close_text = previous_close.text
            #print(prev_close_text)

            open_val = driver.find_element_by_xpath('//*[@id="chart_tab1"]/div[1]/div[2]/div[2]/dl/dd').text 
            #print(open_val)

            high = driver.find_element_by_xpath('//*[@id="chart_tab1"]/div[1]/div[2]/div[3]/dl/dd').text 
            #print(high)

            low = driver.find_element_by_xpath('//*[@id="chart_tab1"]/div[1]/div[2]/div[4]/dl/dd').text 
            #print(low)

            no_of_trades = driver.find_element_by_css_selector('#chart_tab1 > div:nth-child(1) > div:nth-child(3) > div.col-xs-14.col-sm-2.col-md-3.col-lg-3 > dl > dd')   
            no_of_trades_text = no_of_trades.text
            #print(no_of_trades_text)

            avg_trade_size = driver.find_element_by_xpath('//*[@id="chart_tab1"]/div[1]/div[3]/div[2]/dl/dd').text 
            #print(avg_trade_size)

            volume_traded = driver.find_element_by_css_selector('#chart_tab1 > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > dl > dd')   
            vol_traded_text = volume_traded.text
            #print(vol_traded_text)

            value_traded = driver.find_element_by_css_selector('#chart_tab1 > div:nth-child(1) > div:nth-child(3) > div:nth-child(4) > dl > dd')   
            val_traded_text = value_traded.text
            #print(val_traded_text)

            #data = {}
            #data['stock'] = []
            stock = []
            #data['stock'].append({
            stock.append({    
                'Date': date,
                'Sector': sector_text,
                'Industry': industry_text,
                'Reference No': ref_text,
                'Name': comp_text,
                'Symbol': trading_text,
                'Price': price,
                'Close': prev_close_text,
                'Open': open_val,
                'High': high,
                'Low': low,
                'Change': change_val,
                'Change %': change_percent,
                'No Of Trades': no_of_trades_text,
                'Average Trade Size': avg_trade_size,
                'Volume Traded': vol_traded_text,
                'Value Traded': val_traded_text,
            }) 
            
            with open('TASI_Data_%s.json' % date) as outfile:
                old_data = json.load(outfile)
                stock = old_data + stock
            outfile.close()

            with open('TASI_Data_%s.json' % date, 'w') as outfile:
                #json.dump(stock, outfile, indent=2)
                #json.dump(stock, outfile)
                out = json.dumps(stock, separators=(',', ':'))                                                         
                outfile.write(out + '\n')
            outfile.close()

            driver.execute_script("window.history.go(-1)")

            select = Select(driver.find_element_by_css_selector('#table5_paginate > select'))
            current_page= select.first_selected_option.get_attribute("value")

            if current_page!= y:
                select.select_by_value('{}'.format(y))

b=datetime.now()
print("")
print("Total execution time (seconds) : ", (b-a).total_seconds())

log.close()
driver.quit()
