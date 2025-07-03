# Wikimedia Messages - Kafka Pipeline
## Written by: Joe Merten   07/06/2023
This project demonstrates a kafka pipeline.



## There are three components to this project
1. **docker-compose.yml** - This is a docker file that runs kafka and zookeeper
1. **wiki_producer.py** - This is a python script that feeds the kafka pipelnie from the streaming service stream.wikimedia.org/v2/stream/recentchange
1. **wiki_consumer.py** - This is a python script that reads the kafka pipeline and displays the results.

## Directions
1. Save all three files into a directory.
1. From a command prompt in that directory start the containers for kafka using the command:
   - docker-compose up
1. next, start the consumer from the same directory in another command prompt using the command:
   - python ./wiki_consumer.py
1. finally, run the producer from the same directory in another command prompt using the command:
   - python ./wiki_producer.py

## Output - docker
When the docker containers start, a message will be displayed indicating both sookeeper and kafka are running.


## Output - 

## Output - 
