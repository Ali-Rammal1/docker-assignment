We have 2 python files/applications:
- Producer: using socket library, this application generates a random number every 5 seconds and sends it to the consumer
- Consumer: using socket library, receives the number and saves it in the log.txt file on the docker volume.
- Each application has a dockerfile. There was no need to install any external library.
- The docker-compose.yml is configured to build the images from the docker files, set up a  "bridge" network, and the volume for the log.txt file. It then runs both codes (producer then consumer).


After having all files ready:
- producer.py and consumer.py
- both Dockerfiles
- docker-compose.yml
We use the command: docker-compose build
then docker-compose up

to check the log files, we need to first access the shell of a container using:
docker exec -it <consumer_container_id> sh (we get the id from doing docker ps and get the id of the consumer container)
cd \data
cat logs.txt

This file is being updated every 5 seconds with a new number, which means that the 2 containers are successfully communicating using a bridge network.

When done we stop the two containers and remove (if needed) the containers by doing:
docker-compose down


