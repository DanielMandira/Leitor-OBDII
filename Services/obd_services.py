import obd
from Services.connection import get_connection, close


def _query(cmd: obd.OBDCommand):
    conn = get_connection()
    if not conn:
        print("Não conectado ao OBD-II.")
        return None
    try:
        return conn.query(cmd)
    except Exception as e:
        print(f"Falha na consulta {cmd.name}: {e}")
        return None

def verificar_erros():
    dtc_response = _query(obd.commands.GET_DTC)
    if dtc_response and dtc_response.value:
        print("Códigos de erro encontrados:")
        for code in dtc_response.value:
            print(code)
    else:
        print("Nenhum código de erro encontrado.")
    
def verificar_status():
    status_response = _query(obd.commands.STATUS)
    if status_response and status_response.value:
        print("Status do veículo:")
        print(status_response.value)
    else:
        print("Não foi possível obter o status do veículo.")

def ObterDados():
    rpm = _query(obd.commands.ENGINE_RPM)
    if rpm and rpm.value:
        print("RPM do motor:", rpm.value.magnitude)
    else:
        print("Não foi possível obter RPM do motor.")

    temp = _query(obd.commands.COOLANT_TEMP)
    if temp and temp.value:
        print("Temperatura do motor:", temp.value.magnitude)
    else:
        print("Não foi possível obter a temperatura do motor.")

    speed = _query(obd.commands.SPEED)
    if speed and speed.value:
        print("Velocidade do veículo:", speed.value.magnitude)
    else:
        print("Não foi possível obter a velocidade do veículo.")

    fuel = _query(obd.commands.FUEL_LEVEL)
    if fuel and fuel.value:
        print("Nível de combustível:", fuel.value.magnitude)
    else:
        print("Não foi possível obter o nível de combustível.")


def apagar_erros():
    resp = _query(obd.commands.CLEAR_DTC)
    if resp and (resp.value is None or resp.value):
        print("Códigos de erro apagados (se suportado).")
    else:
        print("Não foi possível apagar os códigos de erro.")

def fechar_conexao():
    close()
    print("Conexão fechada.")

