import os
import obd
from serial.tools import list_ports

_connection = None

def _candidate_ports():
    env_port = os.getenv("OBD_PORT")
    ports = []
    if env_port:
        ports.append(env_port)
    # Prioriza portas detectadas pelo sistema
    try:
        ports += [p.device for p in list_ports.comports()]
    except Exception:
        pass
    # Complementa com scan da lib
    try:
        ports += obd.scan_serial()
    except Exception:
        pass
    # Sugestões comuns no Linux
    ports += ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyACM0", "/dev/ttyACM1"]
    # Remove duplicatas mantendo ordem
    seen = set()
    uniq = []
    for p in ports:
        if p and p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq

def connect(port: str | None = None, fast: bool = False, timeout: int = 2):
    global _connection
    if _connection and _connection.is_connected():
        return _connection

    candidate_ports = [port] if port else _candidate_ports()
    print("Portas candidatas:", ", ".join(candidate_ports) if candidate_ports else "(nenhuma)")

    for p in candidate_ports:
        try:
            conn = obd.OBD(portstr=p, fast=fast, timeout=timeout)
            if conn.is_connected():
                print(f"Conectado a {p}")
                _connection = conn
                return _connection
            else:
                print(f"Falhou conectar em {p}")
        except Exception as e:
            print(f"Erro ao conectar a {p}: {e}")

    # Tentativa final automática sem porta específica
    try:
        conn = obd.OBD(fast=fast, timeout=timeout)
        if conn.is_connected():
            print("Conexão automática bem-sucedida")
            _connection = conn
            return _connection
    except Exception as e:
        print(f"Erro na conexão automática: {e}")

    return None

def get_connection():
    return connect()

def close():
    global _connection
    try:
        if _connection:
            _connection.close()
    finally:
        _connection = None


