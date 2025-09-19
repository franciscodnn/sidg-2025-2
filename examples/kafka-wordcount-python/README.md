## Roteiro para executar essa aplicação

1. Acessar o tutorial disponível no link [App de Demonstração, Kafka](https://kafka.apache.org/41/documentation/streams/quickstart)

2. Realizar os passos (steps) de 1 a 3
- Esses passos serão responsáveis por: subir o servidor Kafka (Broker) e criar os tópicos "streams-plaintext-input" e "streams-wordcount-output"

3. Executar o arquivo python producer.py
```python
# Este arquivo irá escrever (produzir conteúdo) no tópico "streams-plaintext-input"
poetry run python producer.py
```

4. Executar o arquivo python app_word_count.py
```python
# 1. Este arquivo irá ler (consumir conteúdo) do tópico "streams-plaintext-input"
# 2. Em seguida, realizará o processamento de contagem das palavras
# 3. Por fim, irá escrever a contagem de palavras (produzir conteúdo) no tópico "streams-wordcount-output"
poetry run python app_word_count.py
```

5. Executar o arquivo python word_count_consumer.py
```python
# Este arquivo irá ler (consumir conteúdo) do tópico "streams-wordcount-output"
poetry run python word_count_consumer.py
```