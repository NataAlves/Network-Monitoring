import json
from app.database.connection import connection_db
from app.config import CURRENT_FILE

def inserir_dados():
    connection = connection_db
    cursor = connection.cursor()

    with open(CURRENT_FILE, "r") as arquivo:
        dispositivos = json.load(arquivo)
        print('Realizado a leitura e upload do arquivo')

    sql = """
    INSERT INTO dispositivos
    (ip,mac,fabricante,primeiro_acesso)
    VALUES (%s,%s,%s,%s)

    ON DUPLICATE KEY UPDATE
    ip = VALUES(ip),
    fabricante = VALUES(fabricante)
    """

    for dispositivo in dispositivos:
        # Trata dispositivos sem MAC
        mac = None if dispositivo["mac"] == "UNKNOWN" else dispositivo["mac"]

        valores = (
            dispositivo.get("ip"),
            mac,
            dispositivo.get("fabricante"),
            dispositivo.get("data")
        )

        try:
            cursor.execute(sql, valores)

        except Exception as erro:
            print(f"Erro: {erro}")

    connection.commit()

    cursor.close()
    connection.close()

    print("Dados inseridos!")