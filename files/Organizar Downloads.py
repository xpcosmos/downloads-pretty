import os
import shutil

pasta = "C:\\Users\\****\\Downloads"
lista_arquivos = []
lista_dir = []

for diretorio, subpastas, arquivos in os.walk(pasta):
    lista_dir.append(diretorio)
    for arquivo in arquivos:
        lista_arquivos.append(os.path.join(arquivo))

arquivos = []
cont = 0
for i in lista_arquivos:
    arquivos.append(i.split('.'))
    if len(i.split('.')) > 2:
        print(i)
for arquivo in arquivos:
    try:
        if f"{arquivo[0]}.{arquivo[1]}" == 'Organizar Downloads.py':
            pass
        else:   
            if arquivo[1] ==  'pdf':
                if 'nota-fiscal' in arquivo[0]:
                    src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                    des = r"C:\Users\****\OneDrive\Documentos\Pessoais\Blueshift\Notas Fiscais\PDF\{}.{}".format(arquivo[0], arquivo[1])
                    shutil.move(src,des)
                else:
                    src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                    des = r"C:\Users\****\Downloads\PDF\{}.{}".format(arquivo[0], arquivo[1])
                    shutil.move(src,des)
            elif arquivo[1] ==  'docx' or arquivo[1] == 'doc' or arquivo[1] == 'odt':
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                des = r"C:\Users\****\Downloads\Docx\{}.{}".format(arquivo[0], arquivo[1])
                shutil.move(src,des)
            elif arquivo[1] ==  'csv' or arquivo[1] ==  'xlsx':
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                des = r"C:\Users\****\Downloads\Planilhas - Excel e CSV\{}.{}".format(arquivo[0], arquivo[1])
                shutil.move(src,des)
            elif arquivo[1] ==  'pptx':
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                des = r"C:\Users\****\Downloads\PowerPoint\{}.{}".format(arquivo[0], arquivo[1])
                shutil.move(src,des)
            elif arquivo[1] ==  'py':
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                des = r"C:\Users\****\Downloads\Python\{}.{}".format(arquivo[0], arquivo[1])
                shutil.move(src,des)
            elif arquivo[-1] ==  'msi':
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                os.remove(src)         
            elif arquivo[-1] ==  'rar' or arquivo[-1] == 'zip':
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                des = r"C:\Users\****\Downloads\WinRAR\{}.{}".format(arquivo[0], arquivo[1])
                shutil.move(src,des)   
            elif arquivo[-1] ==  'sql':
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                des = r"C:\Users\****\Downloads\SQL\{}.{}".format(arquivo[0], arquivo[1])
                shutil.move(src,des)
            elif arquivo[-1] ==  'xml':
                if 'nota-fiscal' in arquivo[0]:
                    src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                    des = r"C:\Users\****\OneDrive\Documentos\Pessoais\Blueshift\Notas Fiscais\XML\{}.{}".format(arquivo[0], arquivo[1])
                    shutil.move(src,des)
                else:
                    src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                    des = r"C:\Users\****\Downloads\XML\{}.{}".format(arquivo[0], arquivo[1])
                    shutil.move(src,des)  
            elif arquivo[-1] ==  'exe':
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                os.remove(src)  
            else:
                src = r"C:\Users\****\Downloads\{}.{}".format(arquivo[0], arquivo[1])
                des = r"C:\Users\****\Downloads\Outros\{}.{}".format(arquivo[0], arquivo[1])
                shutil.move(src,des) 

    except FileNotFoundError:
        pass
    
    