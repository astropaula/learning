from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.swiss.com.pl/pl/zegarki?search_query=zeppelin').text
soup = BeautifulSoup(html_text, 'lxml')
soup.find('div', class_='product_box product_link').decompose()
watches = soup.find_all('div', class_='product_box product_link')
for watch in watches:
    availability = watch.find('span', class_='iconstatus1').text.replace('h', '')
    if(availability == '24'):
        manufacturer = watch.find('span', class_='product_name').span.text.replace(' ', '')
        img = watch.find('img')['src']
        print(f'''
        Manufacturer: {manufacturer}, 
        Checkout photo: {img}
        ''')
        print('')