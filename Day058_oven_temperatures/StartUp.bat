# Joe's version...
cd oven
docker build -t oven .
cd ..\kafka_producer
docker build -t kafkaproducer .
cd ..\spark
docker build -t spark .
cd ..\zookeeper
docker build -t zookeeper .
cd ..\broker
docker build -t broker .
cd ..
docker compose up