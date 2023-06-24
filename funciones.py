def buscar_por_numero():
        numero = input("Ingrese el número de Ley que busca: ")
        if(len(numero) > 0):
            consulta =(f"SELECT * FROM Leyes WHERE NumeroDeNormativa LIKE '{numero}'".format(numero))
            result = db.ejecutar_conexion(consulta)
            for data in result:
                print(""" 
                    +NÚMERO DE REGISTRO :        {}
                    +TIPO DE NORMATIVA :    {}
                    +NÚMERO DE NORMATIVA :     {}
                    +FECHA DE CREACIÓN :     {}
                    +DESCRIPCIÓN :     {}
                    +CATEGORIA :     {}
                    +JURISDICCIÓN :     {}
                    +ÓRGANO LEGISLATIVO :     {}
                    +PALABRA CLAVE :     {}
                    
                    """.format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
