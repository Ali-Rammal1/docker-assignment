
This project consists of two Python applications (Producer and Consumer) that communicate with each other using Docker containers. The Producer generates a random number every 5 seconds and sends it to the Consumer. The Consumer saves the received number to a `log.txt` file stored in a Docker volume.

## Components:
- **Producer**: Uses the `socket` library to generate a random number every 5 seconds and send it to the Consumer.
- **Consumer**: Uses the `socket` library to receive the number from the Producer and stores it in a `log.txt` file on the Docker volume.

### Docker Setup:
- **Dockerfile for Producer**: Builds an image to run the Producer application.
- **Dockerfile for Consumer**: Builds an image to run the Consumer application.
- **docker-compose.yml**: Configures  the two containers, sets up a **bridge** network for communication, and defines a **Docker volume** for the `log.txt` file.


When all files are ready, we use the command: docker-compose build
then docker-compose up

to check the log files, we need to first access the shell of a container using:
docker exec -it <consumer_container_id> sh 
(we get the id from doing docker ps and get the id of the consumer container)
Then access the data folder and view the log.txt file:
cd \data
cat logs.txt

This file is being updated every 5 seconds with a new number, which means that the 2 containers are successfully communicating using a bridge network.

When done we stop the two containers and remove (if needed) the containers by doing:
docker-compose down


