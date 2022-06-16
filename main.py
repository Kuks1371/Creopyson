from os import stat
import creopyson
import time
import subprocess

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)


def selectDimensionSet(DimensionSetName):
    if DimensionSetName == "W1":
        w = [100, 100, 8, 100, 36, 10]
    elif DimensionSetName == "W2":
        w = [100, 140, 8, 100, 36, 10]
    elif DimensionSetName == "W3":
        w = [100, 180, 8, 100, 36, 10]
    elif DimensionSetName == "W4":
        w = [140, 100, 10, 100, 38, 12]
    elif DimensionSetName == "W5":
        w = [140, 140, 10, 100, 38, 12]
    elif DimensionSetName == "W6":
        w = [140, 180, 10, 100, 38, 12]
    elif DimensionSetName == "W7":
        w = [180, 100, 11, 100, 40, 14]
    elif DimensionSetName == "W8":
        w = [180, 140, 11, 100, 40, 14]
    elif DimensionSetName == "W9":
        w = [180, 180, 11, 100, 40, 14]
    return w

def getExtrudeCount(length):
    switcher = {
        100: 2,
        140: 3,
        180: 4
    }
    return switcher.get(length)

def disableOrEnableExtrudes(A, B):
    if(B == 100):
        c.feature_suppress(name="DZIURA1", status="ACTIVE")
    else:
        c.feature_resume(name="DZIURA1", status="SUPPRESSED")
        c.feature_resume(name="WYPUSTKA1", status="SUPPRESSED")
        c.feature_resume(name="ZAOKR1", status="SUPPRESSED")

    if(A == 100):
        c.feature_suppress(name="DZIURA2", status="ACTIVE")
    else:
        c.feature_resume(name="DZIURA2", status="SUPPRESSED")
        c.feature_resume(name="WYPUSTKA2", status="SUPPRESSED")
        c.feature_resume(name="ZAOKR2", status="SUPPRESSED")

def setDimensions(w):
    exCount1 = getExtrudeCount(w[0])
    exCount2 = getExtrudeCount(w[1])

    c.dimension_set("A", w[0])
    c.dimension_set("B", w[1])
    c.dimension_set("C", w[2])
    c.dimension_set("Ddim", w[3])
    c.dimension_set("E", w[4])
    c.dimension_set("Fdim", w[5])

    creopyson.parameter.set_(c, "ExtrudeCountParam1", value= exCount1)
    creopyson.parameter.set_(c, "ExtrudeCountParam2", value= exCount2)
    c.file_regenerate()

def create_info_file(workPath, DimensionSetName, dimensions, materialName):
    file = open(f'{workPath}/Michal_Sit_13K3.txt', 'w')
    file.write(f'Nazwa: {DimensionSetName}\n')
    for i, char in enumerate('ABCDEF'):
        file.write(f'{char}: {dimensions[i]}\n')
    file.write(f'Nazwa materiału: {materialName}\n')
    mass = c.file_massprops()['mass']
    file.write(f'Masa modelu: {mass}')
    file.close()


print("Wybierz katalog roboczy: ")
workPath = input()

if not c.is_creo_running():
    subprocess.Popen("D:/Programs/PTC/Creo 7.0.1.0/Parametric/bin/parametric.exe")
    time.sleep(80)
try:
    c.creo_cd(workPath)
    c.file_open("model.prt")
except:
    print("Podany plik nie istnieje!")

print("Wybierz zestaw danych:")
print("W1: [A=100, B=100, C=8, D=100, E=36, F=10]")
print("W2: [A=100, B=140, C=8, D=100, E=36, F=10]")
print("W3: [A=100, B=180, C=8, D=100, E=36, F=10]")
print("W4: [A=140, B=100, C=10, D=100, E=38, F=12]")
print("W5: [A=140, B=140, C=10, D=100, E=38, F=12]")
print("W6: [A=140, B=180, C=10, D=100, E=38, F=12]")
print("W7: [A=180, B=100, C=11, D=100, E=40, F=14]")
print("W8: [A=180, B=140, C=11, D=100, E=40, F=14]")
print("W9: [A=180, B=180, C=11, D=100, E=40, F=14]")

try:
    dimensionSetName = input()
    dimensions = selectDimensionSet(dimensionSetName)
    setDimensions(dimensions)
    disableOrEnableExtrudes(dimensions[0], dimensions[1])
except:
    print("Błędna nazwa zestawu!")

material_list = ["Cast_iron_ductile", "Steel_cast", "Steel_medium_carbon"]
print("Wybierz materiał: ")
for i, material in enumerate(material_list):
    print(f"{i}. {material}")
    c.file_load_material_file(material, "D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Ferrous_metals")

materialIndex = int(input())
try:
    c.file_set_cur_material(material_list[materialIndex])
except:
    print("Błędna nazwa materiału!")

c.file_regenerate()

create_info_file(workPath, dimensionSetName, dimensions, material_list[materialIndex])
c.interface_export_file("step")
c.interface_export_file("3dpdf")

print("Czy wstawić model do złożenia? (Y/N)")
input = input()
if input == "Y":
    c.file_open("zlozenie.asm")
    time.sleep(10)
    c.file_assemble("model.prt")
elif input == "N":
    print("Nie wstawiono modelu do zlozenia")
else:
    print("Wybrano nieprawidłową opcję!")
