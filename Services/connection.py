import obd

# Listar portas disponíveis
ports = obd.scan_serial()
print("Portas detectadas: ")

for port in ports:
    try:
        # Conactar ao adaptador OBD-II (Auto detecta)
        connection = obd.OBD(port) # ou obd.OBD("/dev/ttyUSB0") no linux
        if connection.is_conected():
            print(f"Conectado a {port}")
            break
    except Exception as e:
        print(f"Erro ao conectar a {port}: {e}")
        
        
