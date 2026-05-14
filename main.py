from dh_core import *
from auth_layer import *

def run_secure_dh():
    p, g = generate_parameters()

    a = generate_private_key(p)
    b = generate_private_key(p)

    A = generate_public_key(g, a, p)
    B = generate_public_key(g, b, p)

    shared_A = generate_shared_key(B, a, p)
    shared_B = generate_shared_key(A, b, p)

    identity = "Alice-Bob-Session"

    hash_A = create_hash(shared_A, identity)
    hash_B = create_hash(shared_B, identity)

    print("Shared Key A:", shared_A)
    print("Shared Key B:", shared_B)
    print("Hash Match:", verify_hash(hash_A, hash_B))

run_secure_dh()