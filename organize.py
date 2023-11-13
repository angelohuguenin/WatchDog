import os
import shutil
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromDir = "C:/Users/Pichau/Downloads"
toDir = "./"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

#classe Gerenciadora dos eventos
class FilesMovementHandler(FileSystemEventHandler):
    #código para gerenciar o evento de criação no diretório
    def on_created(self,event):
        raiz,ext = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                fileName = os.path.basename(event.src_path)
                print("baixado" + fileName)
                path1 = fromDir + '/' + fileName
                path2 = toDir + '/' + key
                path3 = toDir + '/' + key + '/' + fileName
                time.sleep(1)
                if os.path.exists(path2):

                    print("Diretório Existe...")
                    time.sleep(1)
                                        
                    if os.path.exists(path3):

                        print("Arquivo Já Existe em  " + key + "....")
                        print("Renomeando Arquivo " + fileName + "....")

                        new_fileName = os.path.splitext(fileName)[0] + str(random.randint(0, 999)) + os.path.splitext(fileName)[1]

                        path4 = toDir + '/' + key + '/' + new_fileName

                        print("Movendo " + new_fileName + "....")
                        shutil.move(path1, path4)
                        time.sleep(1)

                    else:
                        print("Movendo " + fileName + "....")
                        shutil.move(path1, path3)
                        time.sleep(1)

                else:
                    print("Criando Diretório...")
                    os.makedirs(path2)
                    print("Movendo " + fileName + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)
                    
#incialização da classe Gerenciadora de eventos
eventHandler = FilesMovementHandler()
# instanciar o Observer
observer = Observer()
# Agende o Observer
observer.schedule(eventHandler, fromDir, recursive = True)
# Startar  o Observer
observer.start()

#Loop para executar constantemente até que uma tecla de interrupção seja pressionada
try: 
    while True:
        time.sleep(2)
        print("Executando")
except KeyboardInterrupt: 
    print("Interropido")
    observer.stop()