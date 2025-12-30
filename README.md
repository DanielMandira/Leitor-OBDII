# Leitor-OBDII

Leitor simples via OBD-II para obter leituras básicas conectando um adaptador ELM327 por USB no Linux.

## Requisitos

- Python 3.10+
- Adaptador OBD-II (ELM327) via USB
- Pacotes: `obd`, `pyserial`

Instalação:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Permissões no Linux (se necessário):

```bash
sudo usermod -a -G dialout "$USER"
# Depois, faça logoff/login ou reinicie a sessão
```

## Uso

Conecte o adaptador OBD-II na porta USB (ex.: `/dev/ttyUSB0`). Em seguida:

```bash
python app.py
```

Se quiser especificar a porta manualmente:

```bash
OBD_PORT=/dev/ttyUSB0 python app.py
```

O app tentará detectar portas automaticamente e exibirá leituras de RPM, temperatura do motor, velocidade e nível de combustível (quando suportados pelo veículo).

