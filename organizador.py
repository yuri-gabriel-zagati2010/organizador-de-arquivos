import os
import shutil

pasta = input('digite o endereco da pasta: ')

arquivos = os.listdir(pasta)

categorias = {

    "documentos": [
        '.pdf', '.docx', '.doc', '.xlsx',
        '.xls', '.pptx', '.ppt', '.txt',
        '.csv', '.rtf', '.odt', '.ods',
        '.odp', '.epub', '.md'
    ],

    "imagens": [
        '.jpg', '.jpeg', '.png', '.gif',
        '.webp', '.svg', '.bmp', '.tiff',
        '.ico', '.psd', '.ai', '.raw'
    ],

    "videos": [
        '.mp4', '.mkv', '.avi', '.mov',
        '.wmv', '.flv', '.webm', '.mpeg', '.3gp'
    ],

    "audios": [
        '.mp3', '.wav', '.flac', '.aac',
        '.ogg', '.m4a', '.wma'
    ],

    "instaladores": [
        '.exe', '.msi', '.apk', '.dmg',
        '.bin', '.bat', '.sh', '.app',
        '.deb', '.rpm'
    ],

    "compactados": [
        '.zip', '.rar', '.7z', '.tar', '.gz', '.iso'
    ],

    "fontes": [
        '.ttf', '.otf', '.woff', '.woff2'
    ]

}

def tipoDeArquivo(extensao):
    
    for categoria, lista_extensoes in categorias.items(): 
        if extensao in lista_extensoes:
           return categoria
    
    return 'outros'

for arquivo in arquivos:

    nome, extensao = os.path.splitext(arquivo)
    
    pastas = os.path.join(pasta, tipoDeArquivo(extensao))

    if not os.path.exists(pastas):
        os.mkdir(pastas)

    origem = os.path.join(pasta, arquivo)
    destino = os.path.join(pastas, arquivo)

    if os.path.isfile(origem):
        shutil.move(origem, destino)

    print(arquivo, '→', tipoDeArquivo(extensao))    

print('pasta organizada com sucesso!')
