from Tuenti import Tuenti

# MAIN
miTuenti = Tuenti("Put Your SID here")
r = miTuenti.setUserStatus("Hello World!")
print r

r = miTuenti.getFriendsData()
#Obetener numeros de telefono de amigos.
for amigo in r[0]["friends"]:
    if amigo["phone_number"] != None:
        print amigo["name"], amigo["surname"], '\n\t Phone: ',amigo["phone_number"]


raw_input("\n\nPresiona una tecla para continuar.....")
