import json
from confluent_kafka import Consumer, KafkaException

# Configuração do consumidor
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'word-count-final-results-group',
    'auto.offset.reset': 'earliest' # Lê desde o início do tópico
}

# Cria a instância do consumidor
c = Consumer(config)

# Tópico de saída da contagem de palavras
topic_out = 'streams-wordcount-output'

print(f"Iniciando o consumidor de resultados. Lendo do tópico '{topic_out}'...")
print("Pressione Ctrl+C para sair.")
c.subscribe([topic_out])

try:
    while True:
        # Busca por novas mensagens a cada 1 segundo
        #   - c.poll(1.0) retorna Message, se houver; ou
        #   - None se o tempo expirar
        msg = c.poll(1.0)
        
        # Nenhuma mensagem recebida no tópico streams-wordcount-output
        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                # Fim da partição
                continue
            else:
                print(f"Erro do consumidor: {msg.error()}")
                break

        # A chave (key) é a palavra, e o valor (value) é a contagem
        word = msg.key().decode('utf-8')
        count = msg.value().decode('utf-8')
        
        print(f"Resultado -> Palavra: '{word}' | Contagem: {count}")
        
    print("-" * 10)
    
except KeyboardInterrupt:
    pass
finally:
    c.close()
