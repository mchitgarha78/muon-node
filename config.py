from pyfrost.network.libp2p_base import PROTOCOLS_ID


VALIDATED_CALLERS = {
    '16Uiu2HAmSv27HvK2aHYHEhRU4fdH6FWTdhDnPWekKj2bQpHi4Lgp': [PROTOCOLS_ID['round1'], PROTOCOLS_ID['round2'], PROTOCOLS_ID['round3'], PROTOCOLS_ID['generate_nonces'], PROTOCOLS_ID['sign']],
    '16Uiu2HAmGVUb3nZ3yaKNpt5kH7KZccKrPaHmG1qTB48QvLdr7igH': [PROTOCOLS_ID['sign'], PROTOCOLS_ID['generate_nonces']]
}
