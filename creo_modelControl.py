import creopyson
import subprocess
from fileinput import filename
from unicodedata import name

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)
c.server

def info():
    print(f"Biezacy katalog roboczy: {c.creo_pwd()} \n Obecny material: {c.file_get_cur_material()} \n Jednostki dlugosci obiektu: {c.file_get_length_units()} \nJednostki masy obiektu: {c.file_get_mass_units()}")
    print(f"Cechy modelu: {c.parameter_list()} \n Dokladnosc modelu{c.file_get_accuracy()}")

if c.is_creo_running() == False:
    subprocess.Popen("D:/Programs/PTC/Creo 7.0.1.0/Parametric/bin/parametric.exe")
    pass

directory = input("Podaj katalog roboczy: \n")
c.creo_cd(directory)
print(c.creo_pwd())

file_name = input("Podaj nazwe pliku ktory chcesz otworzyc: \n")
c.file_open(file_name)
c.file_rename("model_MS.prt")
info()

new_directory_path = input("Podaj nowy katalog: \n")
c.creo_cd(new_directory_path)

path_mat = "D:/Programs/PTC/Creo 7.0.1.0/Common Files/text/materials-library/Standard-Materials_Granta-Design/Ferrous_metals"
c.file_load_material_file("Cast_iron_gray.mtl", path_mat)
c.file_set_cur_material("Cast_iron_gray.mtl")

c.file_save()
c.interface_export_file("STEP")
print("Zapisano model w formacie stp w nowo wybranym katalogu.")

c.file_close_window()