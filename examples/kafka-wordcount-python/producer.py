import sys
from confluent_kafka import Producer

# Configuração do produtor
config = {
    'bootstrap.servers': 'localhost:9092'
}

# Cria a instância do produtor
p = Producer(config)

# Tópico de entrada
topic_in = 'streams-plaintext-input'

print("Produtor interativo iniciado. Digite as linhas de texto (Ctrl+C para sair)...")
print("-" * 50)

try:
    # Lê a entrada do teclado linha por linha
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Envia cada linha como uma mensagem
        try:
            p.produce(topic_in, value=line.encode('utf-8'))
            print(f"-> Enviado: '{line}'")
            p.flush()
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

except KeyboardInterrupt:
    print("\nEncerrando o produtor...")
finally:
    # Fecha o produtor
    p.flush()
    print("Produtor finalizado.")
