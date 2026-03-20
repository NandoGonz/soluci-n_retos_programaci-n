"""Tenga un diccionario de contactos con nombre y teléfono.

Permita al usuario:

Ver todos los contactos.

Agregar un contacto.

Eliminar un contacto.

Buscar un contacto."""

agenda_contactos = {}


while True:
    print("#" * 30)
    print("1. Ver todos los contactos")
    print("2. Agregar un contacto")
    print("3. Eliminar un contacto")
    print("4. Buscar un contacto")
    print("0. Salir")
    print("#" * 30)
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        if agenda_contactos:
            print("📒 Contactos en la agenda:")
            for contacto, telefono in agenda_contactos.items():
                print(f"➡️  {contacto}: {telefono}")
        else:
            print("❌ La agenda está vacía.")

    elif opcion == "2":
        contacto = input("Ingrese el nombre del contacto: ").title().strip()
        telefono = int(input("Ingrese el número del contacto: "))
        nuevo_contacto = {contacto: telefono}
        agenda_contactos.update(nuevo_contacto)
        print("✅ Contacto agregado con exito a la agenda")

    elif opcion == "3":
        contacto = input("Ingrese el nombre del contacto: ").title().strip()
        if contacto in agenda_contactos:
            del agenda_contactos[contacto]
            print("✅ Contacto eliminado exitosamente de la agenda")
        else:
            print(
                "❌ No se puede eliminar ese contacto, no existe o no ha sido registrado"
            )

    elif opcion == "4":
        contacto = input("Ingrese el nombre del contacto: ").title().strip()
        if contacto in agenda_contactos:
            print(
                f"✅ El contacto se encuentra registrado con el telefono {agenda_contactos[contacto]}"
            )

        else:
            print("❌ El contacto no existe")

    elif opcion == "0":
        print("🎉 Gracias por usar nuestra agenda")
        break
