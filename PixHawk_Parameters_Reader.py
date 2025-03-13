from pymavlink import mavutil


def reader_params(file_path):
    parameters = {"Parameter_Name": [], "Value": [], "Default_Value": []}


    connection = mavutil.mavlink_connection(file_path)
    data_read = connection.recv_match(type = "PARM")


    while data_read:
        parameters["Parameter_Name"].append(data_read.Name)
        parameters["Value"].append(data_read.Value)
        parameters["Default_Value"].append(data_read.Default)


        data_read = connection.recv_match(type = "PARM")


    for i in range(0,1172):
        print(parameters["Parameter_Name"][i], end=" | ")
        print(parameters["Value"][i],end=" | ")
        print(parameters["Default_Value"][i])



reader_params("/home/brino/Documents/Log_Quadrado.BIN")



