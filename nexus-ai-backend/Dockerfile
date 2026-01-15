# Step 1: Use a lightweight version of Python 3.12 (Slim version)
FROM python:3.12-slim

# Step 2: Create a folder inside the container for our app
WORKDIR /app

# Step 3: Install system tools required for some Python libraries
# 'build-essential' is often needed for math/AI libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy only the requirements file first
# This helps Docker "cache" the installation so it's faster next time
COPY requirements.txt .

# Step 5: Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of our code into the container
COPY . .

# Step 7: Tell the world we are listening on port 8000
EXPOSE 8000

# Step 8: The command to start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]