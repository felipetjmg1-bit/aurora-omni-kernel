/* Copyright (C) 2026 Felipe Marcos de Abreu Aquino - Impulso Digital Soluções em I.A. - Todos os direitos reservados. */

from fastapi import FastAPI

app = FastAPI(title="Aurora Omni-Kernel Bridge")

@app.get("/")
async def root():
    return {"message": "Aurora Omni-Kernel Bridge API is active"}
