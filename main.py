from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




def print_hi(name):
    driver = webdriver.Chrome()
    driver.get("https://kpfu.ru/studentu/ucheba/raspisanie")

    write_elem= driver.find_element_by_id("p_group_name")
    print(type(write_elem))

    write_elem.send_keys("09-821")
    write_elem.send_keys(Keys.ENTER)
    # write_elem.send_keys(Keys.RETURN)
    time.sleep(2)
    html_page = driver.page_source
    soup = BeautifulSoup(html_page, 'html5lib')
    table = soup.findChildren('table')
    my_table = table[len(table)-1]

    rows = my_table.findChildren(['th', 'tr'])
    print("VVEDITE DEN NEDELI")
    a=int(input())
    for row in rows:
        i = -1
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.text
            i += 1
            if a < 7 and a > 0:

                if i == 0:
                    print(value)

                if i == a:
                    print(value)
            else:
                print("sth wrong")

if __name__ == '__main__':
    print_hi('PyCharm')

