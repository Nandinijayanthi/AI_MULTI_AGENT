from pydantic import BaseModel, ValidationError

class FlowBitSchema(BaseModel):
    id: str
    timestamp: str
    data: dict

def parse_json(input_json: dict):
    try:
        parsed = FlowBitSchema(**input_json)
        return {"status": "valid", "data": parsed.dict()}
    except ValidationError as e:
        return {"status": "error", "message": str(e)}