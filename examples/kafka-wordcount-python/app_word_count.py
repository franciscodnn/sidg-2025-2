import json
from confluent_kafka import Consumer, KafkaException, Producer

# Configuração do consumidor
config_consumer = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'wordcount-group',
    'auto.offset.reset': 'earliest'
}

# Configuração do produtor para o tópico de saída
config_producer = {
    'bootstrap.servers': 'localhost:9092'
}

# Instâncias do produtor e consumidor
c = Consumer(config_consumer)
p = Producer(config_producer)

# Tópicos de entrada e saída
topic_in = 'streams-plaintext-input'
topic_out = 'streams-wordcount-output'

# Dicionário para armazenar a contagem de palavras
word_counts = {}

def delivery_report(err, msg):
    """Callback de confirmação de entrega do produtor."""
    if err is not None:
        print(f"Erro ao entregar a mensagem: {err}")
    # else:
    #     print(f"Mensagem entregue com sucesso para o tópico '{msg.topic()}'")

print(f"Iniciando contagem de palavras do tópico '{topic_in}'...")
c.subscribe([topic_in])

try:
    while True:
        msg = c.poll(1.0)
        
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                continue
            else:
                print(f"Erro do consumidor: {msg.error()}")
                break

        # Processamento da mensagem recebida
        line = msg.value().decode('utf-8')
        words = line.lower().split()

        for word in words:
            # Atualiza a contagem da palavra
            word_counts[word] = word_counts.get(word, 0) + 1
            
            # Envia a contagem atualizada para o tópico de saída
            p.produce(topic_out, 
                      key=word.encode('utf-8'), 
                      value=str(word_counts[word]).encode('utf-8'), 
                      callback=delivery_report)
            p.flush()

except KeyboardInterrupt:
    pass
finally:
    c.close()
