from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from agents.classifier_agent import classify_input
from agents.json_agent import parse_json
from agents.email_agent import extract_email_metadata
from agents.pdf_agent import parse_pdf
from memory import store_memory
import json

app = FastAPI(
    title="AI Multi-Agent Ingest API",
    description="API for ingesting text or files. Use /ingest/ to classify and extract information from your input.",
    version="1.0"
)

# ✅ Add this block to fix CORS error:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Info"])
def root():
    return {
        "message": "Welcome to the AI Multi-Agent Ingest API!",
        "usage": {
            "POST /ingest/": {
                "description": "Classify and extract information from text or file.",
                "fields": {
                    "file": "Upload a file (PDF, JSON, Email, etc.)",
                    "text": "Or, enter plain text directly"
                },
                "note": "Provide either a file or text, not both."
            }
        },
        "docs": "/docs"
    }

@app.post("/ingest/", tags=["Ingest"])
async def ingest(
    file: UploadFile = None,
    text: str = Form(None)
):
    if not file and not text:
        return JSONResponse(
            status_code=400,
            content={"error": "No input provided. Please upload a file or provide text."}
        )

    if file:
        content = await file.read()
        source = file.filename
    else:
        content = text.encode()
        source = "form_input"

    try:
        content_text = content.decode(errors='ignore')
    except Exception:
        return JSONResponse(
            status_code=400,
            content={"error": "Failed to decode content."}
        )

    result = classify_input(content_text, source)

    if result.get("format") == "Email":
        parsed = extract_email_metadata(content_text)
    elif result.get("format") == "JSON":
        try:
            parsed = parse_json(json.loads(content_text))
        except Exception:
            parsed = {"message": "Invalid JSON format"}
    elif result.get("format") == "PDF":
        parsed = parse_pdf(content)
    else:
        parsed = {"message": "Unsupported format"}

    store_memory(
        source,
        result.get("format"),
        result.get("intent"),
        str(parsed),
        parsed.get("conversation_id", None) if isinstance(parsed, dict) else None
    )

    return {
        "input_source": source,
        "input_preview": content_text[:100] + ("..." if len(content_text) > 100 else ""),
        "classification": result,
        "parsed_output": parsed,
        "help": "The input was classified and processed. See 'classification' for type and 'parsed_output' for extracted info."
    }
