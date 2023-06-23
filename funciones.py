from os import system
import conexion as conn 
db = conn.baseDeDatos()
import sqlite3
system("cls")

class Leyes():

    def _init_(self):
        self.NumReg = ""
        self.TipNorma = ""
        self.NumNorma = ""
        self.Fecha = ""
        self.Desc = ""
        self.Cat = ""
        self.Jur = ""
        self.OrgLegis = ""
        self.PalCla = ""

    def insertar_nueva_ley( ):
        continuar = True
        while continuar:
            print(".....Ingrese los datos de la nueva ley.....")
            ley = Leyes()
            finRegistro = False
            while (finRegistro!= True):
                ley.NumReg= str(input("INGRESE EL NÚMERO DE REGISTRO DE LA LEY: "))                
                ley.TipNorma = str(input("ELIJA EL TIPO DE NORMATIVA SEGUN LA LEY A CARGAR(Ley, Decreto o Resolución): "))
                ley.NumNorma = str(input("INGRESE EL NÚMERO DE NORMATIVA DE LA LEY: "))
                ley.Fecha = str(input("INGRESE LA FECHA DE CREACIÓN  DE LA LEY: "))
                ley.Desc = str(input("INGRESE UNA BREVE DESCRIPCIÓN DE LA LEY: "))
                ley.Cat = str(input("INGRESE El NÚMERO DE CATEGORIA A LA QUE CORRESPONDE LA LEY (Laboral, Penal, Civil, Comercial, Familia y Suceciones, Agrario y ambiental, Mineria, Derecho informatico: "))
                ley.Jur = str(input("INGRESE EL NÚMERO DE JURISDICCIÓN A LA QUE CORRESPONDE LA LEY (Nacional,Provincial): "))
                ley.OrgLegis= str(input("INGRESE EL ÓRGANO LEGISLATIVO AL QUE CORRESPONDE DE LA LEY: "))
                ley.PalCla = str(input("INGRESE UN PALABRA CLAVE PARA ENCONTRAR LA LEY: "))
                if(len(ley.NumReg) > 0 and len(ley.TipNorma) > 0 and len(ley.NumNorma) > 0 and len(ley.Fecha) > 0 and len(ley.Desc) > 0 and len(ley.Cat) > 0 and len(ley.Jur) > 0 and len(ley.OrgLegis) > 0 and len(ley.PalCla) > 0):
                    consulta = (f"INSERT INTO Leyes (NumeroRegistro,TipoDeNormativa,NumeroDeNormativa,Fecha,Descripcion,Categoria,Jurisdiccion,OrganoLegislativo,PalabraClave) VALUES('{ley.NumReg}','{ley.TipNorma}','{ley.NumNorma}','{ley.Fecha}','{ley.Desc}','{ley.Cat}','{ley.Jur}','{ley.OrgLegis}','{ley.PalCla}')")
                    db.ejecutar_conexion(consulta)
                    print ("LEY INSERTADA CORRECTAMENTE")
                    finRegistro=True
                seguir = input("Desea cargar otra Ley? S/N")
                if seguir == "n" or seguir == "N":                    
                    continuar = False
