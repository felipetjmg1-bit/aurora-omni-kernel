# Copyright (C) 2026 Felipe Marcos de Abreu Aquino - Impulso Digital Soluções em I.A. - Todos os direitos reservados.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from blockchain.ton_integration import AuroraTONConnector

app = FastAPI(title="Aurora Omni-Kernel Bridge")
ton_connector = AuroraTONConnector()

class ValidationRequest(BaseModel):
    wallet_address: str

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Aurora Omni-Kernel Bridge",
        "version": "1.0.0",
        "message": "Sistema de integração de kernel Aurora ativo."
    }

@app.post("/validate-id")
async def validate_id(request: ValidationRequest):
    result = ton_connector.validate_aurora_id(request.wallet_address)
    if result["status"] == "INVALID":
        raise HTTPException(status_code=403, detail=result["error"])
    return result

@app.get("/kernel/status")
async def kernel_status():
    return {
        "kernel_type": "Omni-Kernel",
        "sovereignty_level": "MAX",
        "active_modules": ["Blockchain", "AI-Core", "Vault"],
        "uptime": "99.99%"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
