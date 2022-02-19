import os
import random
import shutil
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/igors/Downloads"
to_dir = "C:/Users/igors/OneDrive/Desktop/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Sound_Files": ['.m4a','.flac','.mp3','.wav','.wma','.aac','.ogg'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg','.dll']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("Inside OnCreated")
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:               
                file_name = os.path.basename(event.src_path)

                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                time.sleep(1)
                if os.path.exists(path2):

                    print("Directory Exists...")
                    time.sleep(1)
                                        
                    if os.path.exists(path3):

                        print("File Already Exists in " + key + "....")
                        print("Renaming File " + file_name + "....")

                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1]

                        path4 = to_dir + '/' + key + '/' + new_file_name

                        print("Moving " + new_file_name + "....")
                        shutil.move(path1, path4)
                        time.sleep(1)

                    else:
                        print("Moving " + file_name + "....")
                        shutil.move(path1, path3)
                        time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)



# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
