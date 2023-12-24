from pyfrost.network.libp2p_base import PROTOCOLS_ID


RUNNER_APP_URL = 'http://127.0.0.1:6000/v1'
REGISTRY_URL = 'http://127.0.0.1:8050/v1'

VALIDATED_CALLERS = {
    '16Uiu2HAmSv27HvK2aHYHEhRU4fdH6FWTdhDnPWekKj2bQpHi4Lgp': [PROTOCOLS_ID['round1'], PROTOCOLS_ID['round2'], PROTOCOLS_ID['round3'], PROTOCOLS_ID['generate_nonces'], PROTOCOLS_ID['sign']]
}