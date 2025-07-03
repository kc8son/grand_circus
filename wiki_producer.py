####################################################################################################
#
#   Date Written: 07/06/2023        By Joseph P. Merten
#   This is the wiki producer from the
#   Wikimedia Messages - # Kafka Pipeline assignment
#
####################################################################################################
#   imports
from kafka import KafkaProducer

####################################################################################################
#   Set up kafka variables.
KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "test")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.3.1")
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
)

####################################################################################################
#   API variable and call
wiki_url = "https://stream.wikimedia.org/v2/stream/recentchange"
response = requests.get(wiki_url, stream=True)
print(response)

####################################################################################################
#   Process 10 messages
print("Starting...")
i = 0
for message in response.iter_lines():
    if message:
        print(f"Sending message #{i}...")
        producer.send(
            KAFKA_TOPIC_TEST, message
        )
        i += 1
        if i > 10:
            break
producer.flush()

