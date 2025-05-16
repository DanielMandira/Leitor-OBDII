import obd
import connection


def verificar_erros():    
    # Verificar códigos de erro
    dtc_response = connection.query(obd.commands.GET_DTC)
    if dtc_response.value:
        print("Códigos de erro encontrados:")
        for code in dtc_response.value:
            print(code)
    else:
        print("Nenhum código de erro encontrado.")
    
def verificar_status():    
    # Verificar o status do veículo
    status_response = connection.query(obd.commands.STATUS)
    if status_response.value:
        print("Status do veículo:")
        print(status_response.value)
    else:
        print("Não foi possível obter o status do veículo.")

def ObterDados():        
    # Verificar dados do veículo
    vehicle_data_response = connection.query(obd.commands.ENGINE_RPM)
    if vehicle_data_response.value:
        print("Dados do veículo:")
        print("RPM do motor:", vehicle_data_response.value.magnitude)
    else:
        print("Não foi possível obter os dados do veículo.")


    # Verificar temperatura do motor
    temperature_response = connection.query(obd.commands.COOLANT_TEMP)
    if temperature_response.value:
        print("Temperatura do motor:", temperature_response.value.magnitude)
    else:
        print("Não foi possível obter a temperatura do motor.")


    # Verificar velocidade do veículo
    speed_response = connection.query(obd.commands.SPEED)
    if speed_response.value:
        print("Velocidade do veículo:", speed_response.value.magnitude)
    else:
        print("Não foi possível obter a velocidade do veículo.")


    # Verificar pressão do óleo
    oil_pressure_response = connection.query(obd.commands.OIL_PRESSURE)
    if oil_pressure_response.value:
        print("Pressão do óleo:", oil_pressure_response.value.magnitude)
    else:
        print("Não foi possível obter a pressão do óleo.")


    # Verificar nível de combustível
    fuel_level_response = connection.query(obd.commands.FUEL_LEVEL)
    if fuel_level_response.value:
        print("Nível de combustível:", fuel_level_response.value.magnitude)
    else:
        print("Não foi possível obter o nível de combustível.")


    # Verificar velocidade do veículo
    speed_response = connection.query(obd.commands.SPEED)
    if speed_response.value:
        print("Velocidade do veículo:", speed_response.value.magnitude)
    else:
        print("Não foi possível obter a velocidade do veículo.")


def apagar_erros():
    # Apagar os códigos de erro
    clear_dtc_response = connection.query(obd.commands.CLEAR_DTC)
    if clear_dtc_response.value:
        print("Códigos de erro apagados.")
    else:
        print("Não foi possível apagar os códigos de erro.")

def fechar_conexao():
    # Fechar a conexão
    connection.close()
    print("Conexão fechada.")

