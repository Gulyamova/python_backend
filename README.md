# Microservices Project

This project is a demonstration of a microservices architecture implemented in Python using FastAPI. It consists of three microservices that simulate basic functionality for order processing, user authentication, and order handling with fictional logic and delays for showcasing interaction between services. Additionally, it includes tests using the pytest library to verify the functionality.

## Microservices Overview

1. **Main Service**:
   - Responsible for creating orders.
   - Simulates user authentication and sends orders for processing by other services.
   - Handles POST requests for creating orders via the `/create_order/` route.

2. **Order Service**:
   - Responsible for order processing.
   - Simulates order processing with delays.
   - Handles GET requests for processing orders via the `/process_order/{order_id}` route.

3. **Authentication Service**:
   - Responsible for user authentication.
   - Simulates user authentication with delays.
   - Handles POST requests for authenticating users via the `/authenticate/` route.
## Getting Started

1. Run proto file
   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. order_service.proto
2. Run each microservice separately:
  ```bash
  uvicorn main_service:app --host 0.0.0.0 --port 8000
  uvicorn order_service:app --host 0.0.0.0 --port 8001
  uvicorn auth_service:app --host 0.0.0.0 --port 8002
```
3. Run tests using pytest:
   ```bash
   pytest
