import pathlib
import shutil
import os, ctypes
import time

def verify_admin():
	try:
		is_admin = os.getuid() == 0
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() == 1

	if is_admin != 1:
		msg_box = ctypes.windll.user32.MessageBoxW(0, "Execute o arquivo como administrador para continuar!", "Erro de permissão", 5)
		if msg_box == 4:
			verify_admin()
		elif msg_box == 2:
			exit()

def delete_files_and_dirs(path):
	for file_name in os.listdir(path):
		file = f"{path}{file_name}"

		if os.path.isdir(file):
			print(f"Deleting folder: \"{file}\"")
			shutil.rmtree(file, ignore_errors=True)

		if os.path.isfile(file):
			try:
				os.remove(file)
			except PermissionError:
				print(f"File \"{file}\" could not be deleted.")
				continue

			print(f"Deleting file: \"{file}\"")

def exec(drive, user):
    delete_files_and_dirs(f"{drive}/Windows/Temp/")
    delete_files_and_dirs(f"{drive}/Windows/Prefetch/")
    delete_files_and_dirs(f"{drive}/Users/{user}/AppData/Local/Temp/")

verify_admin()

while (True):
    exec(pathlib.Path.home().drive, os.path.expanduser("~").split("\\")[-1])
    print("Done.")
    time.sleep((1 * 60 * 60) * 6)
