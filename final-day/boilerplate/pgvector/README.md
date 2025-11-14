Ensure Docker is available on your system

# On Linux/MAC
Run `bash run-pg-vector.sh`
This should create a folder called pgdata which will contain your postgres data 

# On Windows 
Copy the content of run-pg-vector.sh and past in a shell with docker installeed

---

Run `docker ps` to confirm your pgvector instance is running

your DB URL should be 
DATABASE_URL=postgresql://postgres:test@localhost/postgres