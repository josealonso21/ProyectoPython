import pandas as pd
from funciones import *


# Llamando a la función de comandos
opcion = comandos()

if opcion == 1: # Create
    dictAutos = ingreso_datos()
    df = pd.DataFrame([dictAutos], columns=['MARCA', 'FABRICACION', 'COLOR', 'PRECIO', 'ESTADO'])
    try:
        first_read = pd.read_csv('autos.csv')
        df.to_csv('autos.csv', header=False, mode='a',index=False)
    except OSError as e:
        df.to_csv('autos.csv', mode='a',index=False)

    print('\nAUTO REGISTRADO')

elif opcion == 2: # Read
    try:
        df = pd.read_csv('autos.csv')
        df2 = df.loc[df['ESTADO'] != 'vendido']
        print(df2.to_string(index=False))
    except FileNotFoundError as e:
        print('Aún no se han ingresado datos.')

else: # Update
    while True:
        try:
            datos = pd.read_csv('autos.csv')
            dictUpdate = ingreso_datos()
            m_marca = (datos['MARCA']==dictUpdate['MARCA'])
            m_fabricacion = (datos['FABRICACION']==dictUpdate['FABRICACION'])
            m_color = (datos['COLOR']==dictUpdate['COLOR'])
            m_precio = (datos['PRECIO']==dictUpdate['PRECIO'])
            try:
                encontrado=datos.index[m_marca & m_fabricacion & m_color & m_precio].tolist()
                datos.loc[encontrado[0],'ESTADO']='vendido'
                datos.to_csv('autos.csv',index=False)
                df = pd.read_csv('autos.csv')
                print(df.to_string(index=False))
                break
            except IndexError as e:
                print('Los datos ingresados no existen o no son validos. Por favor, intente nuevamente')
        except FileNotFoundError as e:
            print('No existen autos para vender. Por favor, registre uno.')
            break