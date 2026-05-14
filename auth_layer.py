# auth_layer.py
import hashlib

def create_hash(shared_key, identity):
    data = str(shared_key) + identity
    return hashlib.sha256(data.encode()).hexdigest()

def verify_hash(hash1, hash2):
    return hash1 == hash2