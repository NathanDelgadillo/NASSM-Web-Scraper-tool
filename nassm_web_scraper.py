import csv


def read_csv(filepath):
    data = []
    with open(filepath, mode='r', newline ='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data# each row is an OrderedDict


california = read_csv('files/california.csv')
colorado = read_csv('files/colorado.csv')
florida = read_csv('files/florida.csv')
illinois = read_csv('files/illinois.csv')
maryland_virginia = read_csv('files/maryland_virginia.csv')
massachusetts = read_csv('files/massachusetts.csv')
new_jersey = read_csv('files/new_jersey.csv')
oregon = read_csv('files/oregon.csv')
pennsylvania = read_csv('files/pennsylvania.csv')
texas = read_csv('files/texas.csv')
washington = read_csv('files/washington.csv')

state_list = ['california','colorado','florida','illinois', 'maryland_virginia', 'massachusetts',
              'new_jersey','oregon', 'pennsylvania', 'texas', 'washington']


new_list = []
for state in state_list:
    if state == 'california':
        for item in california:
            item['state']=state
            new_list.append(item)
    if state == 'colorado':
        for item in colorado:
            item['state']=state
            new_list.append(item)
    if state == 'florida':
        for item in florida:
            item['state'] = state
            new_list.append(item)
    if state == 'illinois':
        for item in illinois:
            item['state'] = state
            new_list.append(item)
    if state == 'maryland_virginia':
        for item in maryland_virginia:
            item['state'] = state
            new_list.append(item)

    if state == 'massachusetts':
       for item in massachusetts:
            item['state'] = state
            new_list.append(item)

    if state == 'new_jersey':
        for item in new_jersey:
            item['state'] = state
            new_list.append(item)

    if state == 'oregon':
        for item in oregon:
            item['state'] = state
            new_list.append(item)

    if state == 'pennsylvania':
        for item in pennsylvania:
            item['state'] = state
            new_list.append(item)

    if state == 'texas':
        for item in texas:
            item['state'] = state
            new_list.append(item)

    if state == 'washington':
        for item in washington:
            item['state'] = state
            new_list.append(item)

missing_email = []

for item in new_list:
    for k,v in item.items():
        if []

for item in new_list:
    email = item['Contact (Email)']
    if email == '':
        item['Contact (Email)'] = 'N/A'
        missing_email.append(item)

print(missing_email)


for item in missing_email:
    company = item['Client ']
    for item2 in scraped_list:
        master = item2['company_name']
        if company == master:
            email = item2['contact_email']
            print(f'found it! {email}')



for item in new_list:
    company = item['Client ']
    for item2 in scraped_list:
        master = item2['company_name']
        if company == master:
            email = item2['contact_email']
            print(f'found it! {email}')






import requests
from bs4 import BeautifulSoup

url = "https://www.nasmm.org/find-a-move-manager/list/?country=us"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Each listing may be inside a div or table row - inspect HTML to adjust
#for listing in soup.select('.results'):

container = soup.find('div', class_='results')
# hypothetical class
scraped_list = []
for listing in container.find_all('li', class_='smm-block'):
    company_elem = listing.find('h5')
    company_name = company_elem.text.strip() if company_elem else ''
    print (company_name)
    email_elem = listing.find('a', href=lambda x: x and x.startswith('mailto:'))
    email = email_elem['href'].replace('mailto:', '') if email_elem else ''
    new_dic = {}
    new_dic['company_name']= company_name
    new_dic['contact_email'] = email
    scraped_list.append(new_dic)
    print (email)


for item in california:
    item['State']='CA'

for item in colorado:
    item['State'] = 'CO'

for item in florida:
    item['State'] = 'FL'

for item in illinois:
    item['State'] = 'IL'

for item in maryland_virginia:
    item['State'] = 'MD/VA'

for item in massachusetts:
    item['State'] = 'MA'

for item in new_jersey:
    item['State'] = 'NJ/NY'

for item in oregon:
    item['State'] = 'OR'

for item in pennsylvania:
    item['State'] = 'PA'

for item in texas:
    item['State'] = 'TX'

for item in washington:
    item['State'] = 'WA'


for data in mycsv:
    for k,v in data.items():
        if v == '':
            v = 'test'
            data[k]=v


for item in state_list:
    for item2 in item:
        new_list.append(item2)



combined_list = []
for item in california:
    combined_list.append(item)


def export_dict_to_csv(data, filepath):
    """
    Exports a list of dictionaries to a CSV file.

    Parameters:
    - data: list of dictionaries, each representing a row
    - filepath: path to the output CSV file
    """
    if not data:
        raise ValueError("Data list is empty. Nothing to write.")

    # Extract the header from the keys of the first dictionary
    headers = data[0].keys()

    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data exported successfully to {filepath}")


export_dict_to_csv(mycsv,'Raul_updated.csv')


combined_list = []

for item in california:
    combined_list.append(item)