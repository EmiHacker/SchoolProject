import argparse
import sys
import configparser
import os
import bs4
from bs4 import BeautifulSoup as bs #pip install beautifulsoup4
import requests
import re
import json
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image

#funcion principal
#
def main(link):
    page(link)

#se busca la url y se nos dice si nos deja entrar
#
def page(link):
    print("Pagina Investigada: ")
    print(link+"\n")
    page=requests.get(link)
    if page.status_code==200:
        print('Status code:')
        print(page.status_code)
        print('\n')
        descargar(link)
        soup=bs(page.content, 'html.parser')
        results=soup.find_all("p")
        info=results[0].get_text()
    
#se descargan las imagenes de la url 
#
def descargar(site):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"}
    response=requests.get(site, headers=headers)
    soup=bs(response.text,"html.parser")
    print(site)
    
    for link in soup.find_all("img"):
        
        url=link.get("src",'scrset')
        filename=re.search(r"/([\w_-]+[.](jpg))",url)
        
        if not filename:
            pass
        else:
            try:
                with open("metadataimgPIA/"+filename.group(1),"wb") as f: #metadataimgPIA/ is a directory on my PC
                    if "http" not in url:
                        url="{}{}".format(site,url)
                    response=requests.get(url)
            except Exception as e:
                pass
    pass

#
def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
#   
def printMeta():
    ruta = ''#Change this rute
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            direction=(os.path.join(root, name))
            m=("[+] Metadata for file: %s" %(name))
            archivo=(str(name)+'.txt')
            f=open(str(name)+'.txt','w')
            with open(str(name)+'.txt','a') as f:
                f.write(direction)
                f.write(m)
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    meta=("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    f.write(meta,'a')
                    f.close()
            except:
                import sys, traceback
#
def SendingtoEncrypt():
    ruta = ''#Change this rute
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if re.findall('.txt$',name):
                print('\n')
                print(name)
                archivos=open(name,'r')
                texto=archivos.readlines()
                print(texto)
                archivos.close
                texto=(str(texto))
                texto=texto.upper()
                print(texto)
                textoEnc = Encriptar(texto)
                print(textoEnc)
                with open(name+'_encriptado.txt','w') as encriptado :
                    encriptado.write(textoEnc)
                    encriptado.close()

#Encriptamos la informacion dada
def Encriptar(Texto):
    TextoEnc = '' #str vacio
    for letra in Texto: #recorro Frase letra por letra
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                TextoEnc += y #fraseEnc.append(y)
                encontrado = True
        if not encontrado: #if encontrado == False
                            # if encontrado != True
            TextoEnc += letra
    return TextoEnc

abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
}
#especie de menu para ingresar la configuracion
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', type=str, help='A website link')
    parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='config file')
    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        # Transforming values into integers
        args.l = str(config['CONFIG']['l'])
    main(args.l)
                        
printMeta()
SendingtoEncrypt()
