# evaluation.py
import time
from mitm_attack import mitm_simulation
from auth_layer import create_hash, verify_hash

def test_detection(trials=100):
    detected = 0

    identity = "Alice-Bob-Session"

    for _ in range(trials):
        shared_A, shared_B = mitm_simulation()

        hash_A = create_hash(shared_A, identity)
        hash_B = create_hash(shared_B, identity)

        if not verify_hash(hash_A, hash_B):
            detected += 1

    return detected / trials


start = time.time()
rate = test_detection(500)
end = time.time()

print("MITM Detection Rate with Authentication:", rate)
print("Execution Time:", end - start)