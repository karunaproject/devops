# DevOps
## How to run
1. Install docker and docker compose 
- https://docs.docker.com/engine/install/
- https://docs.docker.com/compose/install/
2. Copy FE static files to fe directory (currently in FE is example index.html).
3. Current BE is only example, the final version will be prepared for java .jar file runing.
4. Run ```sudo docker compose --env-file .env up``` (for prod will be different .env file).