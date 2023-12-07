import types
from typing import Dict
from muon_frost_py.abstract.node.validators import Validators
from libp2p.typing import TProtocol
from types import FunctionType
from node_config import VALIDATED_CALLERS

class NodeValidators(Validators):
    def __init__(self) -> None:
        super().__init__()
    
    @staticmethod
    def caller_validator(sender_id: str, protocol: TProtocol):
        if protocol in VALIDATED_CALLERS.get(sender_id, []):
            return True
        return False
        
    @staticmethod
    def data_validator(self, sign_function: FunctionType, commitment_list: Dict, input_data: Dict):
        pass