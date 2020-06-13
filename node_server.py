from hashlib import sha256
import json
import time


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash


"""
implementing the proof of work algorithm
"""

difficulty = 2

def proof_of_work (self, block):
    block.nonce = 0     ## using brute force, that's the only possible way to figure out the nonce
    computed_hash = block.compute_hash()
    while not computed_hash.startswith('0' * Block.difficulty):
        block.nonce += 1
        computed_hash = block.compute_hash()

    return computed_hash
