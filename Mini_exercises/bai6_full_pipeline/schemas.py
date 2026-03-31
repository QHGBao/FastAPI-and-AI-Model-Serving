from pydantic import BaseModel

class PredictionRequest(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    floors: int
    property_type: str
    furniture: str
    legal_status: str
    distance_to_center: float