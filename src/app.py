from fastapi import FastAPI
from fastapi.middleware import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=["*"],
    allow_credentials=False,
    allow_methods=["*"],
)

@app.get("/health", tags=["Health"])
async def get_health():
    return {'message':'servidor funcionando!'}
