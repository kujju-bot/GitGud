from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import json
import requests
import dotenv

dotenv.load_dotenv()

os.makedirs("output", exist_ok=True)

app = FastAPI()

# CORS configuration
cors_origins = os.getenv("CORS_ORIGINS", "*")
if not cors_origins or cors_origins.upper() == "NONE":
    allow_origins = ["*"]
else:
    allow_origins = [origin.strip() for origin in cors_origins.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

progress = 0