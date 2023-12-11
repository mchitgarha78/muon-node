import types
from typing import Dict
from muon_frost_py.abstract.node.validators import Validators
from libp2p.typing import TProtocol
from types import FunctionType
from node_config import VALIDATED_CALLERS
import requests

class NodeValidators(Validators):
    def __init__(self) -> None:
        super().__init__()
    
    @staticmethod
    def caller_validator(sender_id: str, protocol: TProtocol):
        if protocol in VALIDATED_CALLERS.get(sender_id, []):
            return True
        return False
    
    @staticmethod
    def data_validator(self, input_data: Dict):
        url = 'http://127.0.0.1:6000'
        headers = {
            "Content-Type": "application/json"
        }
        result = requests.post(url=url, headers = headers, data = input_data).json()
        return result
        