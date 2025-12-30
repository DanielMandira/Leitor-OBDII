from Services import obd_services as obdsvc
from Services.connection import connect

def main():
	conn = connect()
	if not conn:
		print("Falha ao conectar ao adaptador OBD-II. Verifique o cabo/porta e permissões (grupo dialout).")
		return 1

	try:
		print("Conexão estabelecida. Lendo status e dados...")
		obdsvc.verificar_status()
		obdsvc.ObterDados()
	finally:
		obdsvc.fechar_conexao()
	return 0

if __name__ == "__main__":
	raise SystemExit(main())