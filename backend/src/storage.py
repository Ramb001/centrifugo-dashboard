from pydantic import BaseModel
from typing import Dict, List
from dataclasses import dataclass

sid_storage: Dict[int, str] = {}
sid_list: List[str] = []


@dataclass
class SidData(BaseModel):
    sid: str
    user_id: int
