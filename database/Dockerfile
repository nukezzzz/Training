FROM mongo:5.0-focal
COPY matches.json /matches.json
CMD mongoimport --host db-service --db cricket --collection matches --type json --file /matches.json --jsonArray





