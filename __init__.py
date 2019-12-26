# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import json
"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "setVars":

    data_ = GetParams("data_")
    vars_ = GetParams("vars_")

    data_ = json.loads(data_.replace("'", '"'))
    vars_ = str(vars_)
    print(data_, vars_)
    cont = 0

    try:
        vars_ = vars_.split(',')

        total_ = len(data_)
        tot_var = len(vars_)

        if tot_var < total_:
            raise Exception('Cantidad de variables menor a cantidad de datos')

        while cont < total_:
            vars = vars_[cont]
            val_ = data_[cont]
            SetVar(vars, val_)
            cont = cont + 1
    except Exception as e:
        PrintException()
        raise e
