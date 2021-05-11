import tkinter
from tkinter import messagebox as mbox, filedialog as fdialog
import win32api as win_api
from hashlib import sha512
import os
import winreg

path = "E:\\LAB\\lab1.exe"


def collecting_computer_information():
    user = "Пользователь: " + win_api.GetUserName()
    computer_name = "Имя компьютера: " + win_api.GetComputerName()
    windows_directory = "Путь к папке OS Windows: " + win_api.GetWindowsDirectory()
    system_directory = "Путь к папке с системными файлами: " + win_api.GetSystemDirectory()
    volume_label = "Метка Тома: " + str(win_api.GetVolumeInformation("E:\\"))
    memory = "Обьем Памяти:" + str(win_api.GetDiskFreeSpace())
    screen_height = "Высота экрана: " + str(win_api.GetSystemMetrics(0))
    keyboard_type = "Тип и подтип клавиатуры: " + str(win_api.GetKeyboardLayout())
    all_info = " ".join([user, computer_name, windows_directory, system_directory, volume_label, memory, screen_height,
                         keyboard_type])
    all_info = sha512(all_info.encode())
    return all_info.hexdigest()


def register_creation(inform):
    REG_NAME = "Ivanchenkov Max"
    name = "Hash_code"
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_NAME)
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_NAME, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, inform)
    winreg.CloseKey(registry_key)


def install_files(chosen_path):
    file_exe = chosen_path + '/' + 'lab2.exe'
    message = True
    if os.path.isfile(file_exe):
        message = mbox.askokcancel("Ошибка", "Файл с таким именем уже присутствует, перезаписать?")
    if message:
        exe = open(file_exe, 'wb')
        file = open(path, 'rb').read()
        exe.write(file)
        exe.close()
        mbox.showinfo("Установка", "Файлы Установлены!")


def ask_path():
    chosen_path = ""
    # if register_creation(collecting_computer_information()):
    (collecting_computer_information())
    chosen_path = fdialog.askdirectory()
    if chosen_path != '':
        install_files(chosen_path)
    else:
        mbox.showerror("Ошибка", "Информация не добавлена в регистр!")


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("installer")
    root.geometry("200x200+500+100")
    install = tkinter.Button(text="instal", command=ask_path, font="Arial 11", activebackground='#D9BD32', background='#D9BD32')
    install.place(relx=0.20, rely=0.20, width=160)
    root.mainloop()
