from pyfrost.network.abstract import Validators
from config import VALIDATED_CALLERS
from libp2p.typing import TProtocol
from typing import Dict
import hashlib
import os
import json
import requests


class NodeValidators(Validators):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def caller_validator(sender_id: str, protocol: TProtocol):
        if protocol in VALIDATED_CALLERS.get(str(sender_id), {}):
            return True
        return False

    @staticmethod
    def data_validator(input_data: Dict):
        headers = {
            "Content-Type": "application/json"
        }
        res: Dict = requests.post(
            url=os.getenv('RUNNER_APP_URL'), headers=headers, json=input_data).json()
        if not res.get('hash'):
            hash_obj = hashlib.sha3_256(json.dumps(res).encode())
            res['hash'] = hash_obj.hexdigest()
        return res
