#!/bin/bash
# uvicorn server:app --host 0.0.0.0 --port 10000
# uvicorn backend.server:app --reload
#!/bin/bash
uvicorn backend.server:app --host 0.0.0.0 --port 8000 --reload
