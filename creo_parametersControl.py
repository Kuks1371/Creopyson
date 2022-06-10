import creopyson
c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)

def dimset(name, value):
    if value <= 0:
        raise Exception("niepoprawna wartosc! parametr: " + name)
    c.dimension_set(name, value)

def indimset(text, name):
    print(text)
    while True:
        try:
            dimset(name, int(input()))
            break
        except:
            print("zla wartosc!")


c.creo_cd("D:\\box")
c.file_open("box.prt")
indimset("podaj dlugosc", "l")
indimset("podaj szerokosc", "w")
indimset("podaj wysokosc", "h")
indimset("podaj wysokosc tekstu", "t_h")
indimset("podaj odleglosc tekstu od boku", "t_l")
indimset("podaj wypuklosc tekstu", "t_w")

print("podaj tekst")
creopyson.parameter.set_(c, "T", input())

c.file_load_material_file("Aluminum_wrought.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Brass_cast.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Gold.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Lead.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Nickel.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Ni-Cr_alloy.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Silver.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Tin.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Titanium.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
c.file_load_material_file("Zinc.mtl","D:\\Programs\\PTC\\Creo 7.0.1.0\\Common Files\\text\\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")

print("wybierz material z listy:")
print(creopyson.file.list_materials(c))
mats = creopyson.file.list_materials(c)

while True:
    try:
        c.file_set_cur_material(input())
        break
    except:
        print("zly material!")

c.file_regenerate()