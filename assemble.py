import creopyson
import subprocess

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)

def creoRunning():
    isRunnig = c.is_creo_running()
    if (isRunnig == True):
        print("Creo is running!")
    else:
        print("Creo is not running")
        subprocess.Popen("D:/Programs/PTC/Creo 7.0.1.0/Parametric/bin/parametric.exe")
        print("Launching Creo...")

def filePath():
    directory = input("Specify working directory: \n")
    c.creo_cd(directory)
    print(c.creo_pwd())
    file = input("Specify file name to open: \n")
    c.file_open(file)


creoRunning()
filePath()

print(c.parameter_list())

c.parameter_set("X_OFFSET", value=300)
c.parameter_set("Y_OFFSET", value=300)
c.parameter_set("Z_OFFSET", value=300)
print("New parameters values set")

c.file_assemble("model4.prt")

c.file_get_transform(csys="ASM_DEF_CSYS")

c.file_assemble("model5.prt")

c.file_get_transform(csys="ACS0")

c.file_save()
c.file_rename("SI_MI.asm")
c.file_save()

try:
    c.drawing_create("a3_drawing.drw")
except Exception as ex:
    print(ex)
    
print(c.file_list())

c.file_open("SI_MI.drw")