from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}

site_dolar = requests.get('https://www.google.com/search?q=dolar&rlz=1C1GCEA_enBR952BR952&oq=dolar&aqs=chrome..69i57j0i271l3.919j0j1&sourceid=chrome&ie=UTF-8', headers=headers)

site_euro = requests.get('https://www.google.com/search?q=euro&rlz=1C1GCEA_enBR952BR952&ei=aZN-YqaPMK701sQPx5WNqAs&ved=0ahUKEwjm5-Om_tz3AhUuupUCHcdKA7UQ4dUDCA8&uact=5&oq=euro&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjILCAAQgAQQsQMQgwEyBAgAEEMyBAgAEEMyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwE6CggAELEDEIMBEEM6BQgAEIAEOgsILhCxAxDHARCjAjoFCC4QgAQ6CAguEIAEELEDSgQIQRgASgQIRhgAUABYoQNghAVoAHABeACAAYIBiAH2A5IBAzAuNJgBAKABAcABAQ&sclient=gws-wiz', headers=headers)

site_libra = requests.get('https://www.google.com/search?q=libra+esterlina&ei=cKKBYoG3Muyq1sQP5I2vwA0&oq=libra+es&gs_lcp=Cgdnd3Mtd2l6EAMYADINCAAQgAQQsQMQRhCCAjIICAAQgAQQsQMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAEIAEMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEOgsIABCABBCxAxCDAToLCC4QgAQQsQMQgwE6CAgAELEDEIMBOgsILhCABBDHARCjAjoOCC4QgAQQsQMQxwEQ0QM6CQgAEEMQRhCCAjoHCAAQsQMQQ0oECEEYAEoECEYYAFAAWKYIYN4TaABwAHgBgAGpBIgBwRGSAQkyLTEuMy4xLjGYAQCgAQHAAQE&sclient=gws-wiz', headers=headers)

site_iene = requests.get('https://www.google.com/search?q=iene&ei=sKSBYvqdNv7M1sQP0tya0As&ved=0ahUKEwj6tfCZ6-L3AhV-ppUCHVKuBroQ4dUDCA4&uact=5&oq=iene&gs_lcp=Cgdnd3Mtd2l6EAMyDAgAELEDEEMQRhCCAjIECAAQQzIICAAQgAQQsQMyBAgAEEMyCAgAEIAEELEDMggIABCABBCxAzIECAAQQzILCAAQgAQQsQMQgwEyBQgAEIAEMgQIABBDOg4ILhCABBCxAxCDARDUAjoOCC4QgAQQsQMQxwEQowI6DgguEIAEELEDEMcBENEDOgsILhCABBDHARCvAToHCAAQsQMQQ0oECEEYAEoECEYYAFAAWMACYMMEaABwAXgAgAGVAYgBsASSAQMwLjSYAQCgAQHAAQE&sclient=gws-wiz', headers=headers)

soup_dolar = BeautifulSoup(site_dolar.content, 'html.parser')
soup_euro = BeautifulSoup(site_euro.content, 'html.parser')
soup_libra = BeautifulSoup(site_libra.content, 'html.parser')
soup_iene = BeautifulSoup(site_iene.content, 'html.parser')

valor_dolar = soup_dolar.find_all('span', class_='DFlfde SwHCTb')[0]
valor_euro = soup_euro.find_all('span', class_='DFlfde SwHCTb')[0]
valor_libra = soup_libra.find_all('span', class_='DFlfde SwHCTb')[0]
valor_iene = soup_iene.find_all('span', class_='DFlfde SwHCTb')[0]

# print(f'O Dolár está na cotação atual em R$ {valor_dolar.text}')
# print(f'O Euro está na cotação atual em R$ {valor_euro.text}')
# print(valor_libra.text)
