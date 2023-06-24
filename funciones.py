def modificar_una_ley():
        LeyModif = Leyes()
        NumNorma = input("INGRESA EL NÚMERO DE NORMATIVA DE LA LEY: ")
        if(NumNorma != 0):
            LeyModif.NumReg = str(input("INGRESE EL NÚMERO DE REGISTRO DE LA LEY: "))
            LeyModif.TipNorma = str(input("ELIJA EL TIPO DE NORMATIVA SEGUN LA LEY A CARGAR: \n 1 --> Ley\n 2 --> Decreto\n 3 --> Resolución\n"))
            LeyModif.NumNorma= str(input("INGRESE EL NÚMERO DE NORMATIVA DE LA LEY: "))
            LeyModif.Fecha = str(input("INGRESE LA FECHA DE CREACIÓN  DE LA LEY: "))
            LeyModif.Desc= str(input("INGRESE UNA BREVE DESCRPCIÓN DE LA LEY: "))
            LeyModif.Cat = str(input("INGRESE El NÚMERO DE CATEGORIA A LA QUE CORRESPONDE LA LEY:  \n 1 --> Laboral\n 2 --> Penal\n 3 --> Civil\n 4 --> Comercial\n 5 --> Familia y Suceciones\n 6 --> Agrario y ambiental\n 7 --> Mineria\n 8 --> Derecho informatico\n"))
            LeyModif.Jur = str(input("INGRESE EL NÚMERO DE JURISDICCIÓN A LA QUE CORRESPONDE LA LEY: \n 1 --> Nacional\n 2 --> Provincial\n"))
            LeyModif.OrgLegis= str(input("INGRESE EL ÓRGANO LEGISLATIVO AL QUE CORRESPONDE DE LA LEY: "))
            LeyModif.PalCla = str(input("INGRESE UN PALABRA CLAVE PARA ENCONTRAR LA LEY: "))
        if(len(LeyModif.NumReg) > 0 and len(LeyModif.NumNorma) > 0 and len(LeyModif.TipNorma) > 0 and len(LeyModif.Desc) > 0 and len(LeyModif.Fecha) > 0 and len(LeyModif.Cat) > 0 and len(LeyModif.Jur) > 0 and len(LeyModif.OrgLegis) > 0 and len(LeyModif.PalCla)):
            consulta = (f"UPDATE Leyes SET NumeroRegistro='{LeyModif.NumReg}',TipoDeNormativa='{LeyModif.TipNorma}',NumeroDeNormativa='{LeyModif.NumNorma}',Fecha='{LeyModif.Fecha}',Descripcion='{LeyModif.Desc}',Categoria='{LeyModif.Cat}',Jurisdiccion='{LeyModif.Jur }', OrganoLegislativo='{LeyModif.OrgLegis}',  PalabraClave='{LeyModif.PalCla}' WHERE NumeroNormativa='{NumNorma}'")
            db.ejecutar_funcion(consulta)
            print("Ley actualizada correctamente!")
        else:
            print("Se require un número de Ley!")
   
 def eliminar_una_ley():
        LeyAEliminar = input("INGRESA EL NÚMERO DE REGISTRO DE LA LEY: ")
        pregunta = input("Está seguro de querer borrar esta ley? S/N ")
        if (pregunta =="S" or pregunta == "s"):
            if(LeyAEliminar != 0):
                consulta = (f"DELETE FROM Leyes WHERE NumeroRegistro = '{LeyAEliminar}'")
                db.ejecutar_conexion(consulta)
                print("Ley eliminada correctamente!")
            else:
                print("Se require ingresar un número de registro")
        else:
            print("Ud ha decidido no eliminar la ley")
