from pyzbar.pyzbar import decode
from PIL import Image
import pandas as pd
from bs4 import BeautifulSoup
import requests

qr=decode(Image.open('qrSAT.png'))
url = qr[0].data.decode()

#response = requests.get('https://siat.sat.gob.mx/app/qr/faces/pages/mobile/validadorqr.jsf?D1=10&D2=1&D3=15010821958_GAAN7506244V4')
response = requests.get(url)

soup_data = BeautifulSoup(response.content, 'html.parser')

# Aqui se obtiene la parte donde se encuentran contenidos los datos 
ext_content = soup_data.find_all('div', {'id':'pageContent'})

# Aqui se obtiene el RFC
class_rfc = list(str(ext_content[0].li))

rfc=""

for i in range (13):
    rfc=rfc+class_rfc[12+i]

# Aqui se obtiene la parte donde se encuentra todos los datos de identificacion

name_scrap=ext_content[0].find_all('tr', class_ ='ui-widget-content')
name_scrap_text=name_scrap[0].td.text

# Aqui se obtiene la parte donde se encuentra todos los datos de ubicacion

name_scrap2=ext_content[0].find_all('table')
name_scrap2_tr=name_scrap2[3].find_all("tr")
name_scrap2_text=name_scrap2_tr[0].td.text

# Aqui se obtiene la parte donde se encuentra todos los datos de fiscales

name_scrap3_tr=name_scrap2[6].find_all("tr")
name_scrap3_text=name_scrap3_tr[0].td.text

# Aqui se obtiene el nombre
nombre=""
for i in range (name_scrap_text.rfind('Nombre:')+7,name_scrap_text.find('Apellido Paterno'),1):
    nombre=nombre+name_scrap_text[i]

# Aqui se obtiene el apellido paterno
paterno=""
for i in range (name_scrap_text.rfind('Paterno:')+8,name_scrap_text.find('Apellido Materno'),1):
    paterno=paterno+name_scrap_text[i]

# Aqui se obtiene el apellido paterno
materno=""
for i in range (name_scrap_text.rfind('Materno:')+8,name_scrap_text.find('Fecha Nacimiento'),1):
    materno=materno+name_scrap_text[i]

# Aqui se obtiene el CP
cp=""
for i in range (name_scrap2_text.rfind('CP:')+3,name_scrap2_text.find('Correo electrónico:'),1):
    cp=cp+name_scrap2_text[i]

# Aqui se obtiene el regimen
regimen=""
for i in range (8,name_scrap3_text.find('Fecha de alta:'),1):
    regimen=regimen+name_scrap3_text[i]
    
#Creamos Data Frame

df=pd.DataFrame()

new_employee={'Nombre':nombre+" "+paterno+ " "+materno,'RFC':rfc, 'CP':cp, 'Regimen':regimen}
df=df.append(new_employee,ignore_index=True)
df.to_csv('Finanzas')
df
