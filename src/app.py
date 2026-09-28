from fastapi import FastAPI
from fastapi.middleware import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin=['*'],
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

@app.get("/health", tags=["Health"])
async def get_health():
    return {'message':'servidor funcionando!'}
