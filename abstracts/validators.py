from pyfrost.network.abstract import Validators
from config import VALIDATED_CALLERS
from libp2p.typing import TProtocol
import os

from typing import Dict
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
        params = input_data.get('data', {}).get('params')
        sign_params = input_data.get('data', {}).get('signParams')
        result = input_data.get('data', {}).get('result')
        res: Dict = requests.post(
            url=os.getenv('RUNNER_APP_URL'), headers=headers, json=input_data).json()
        if not res.get('hash'):
            res['hash'] = ''
        return res
