# dh_core.py
import random

def generate_parameters():
    p = 23  # prime
    g = 5   # primitive root
    return p, g

def generate_private_key(p):
    return random.randint(1, p-1)

def generate_public_key(g, private, p):
    return pow(g, private, p)

def generate_shared_key(public, private, p):
    return pow(public, private, p)