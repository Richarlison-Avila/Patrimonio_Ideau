from config_db import get_connection

try:
    conn = get_connection()
    print("✅ Conexão OK com o banco de dados!")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar:", e)
