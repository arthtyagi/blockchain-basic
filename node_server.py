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


class BlockC:
    # difficulty of our PoW algorithm
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)


    def proof_of_work(self, block):
        block.nonce = 0  # using brute force, that's the only possible way to figure out the nonce
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * BlockC.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash


    def is_valid_proof(self, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * BlockC.difficulty) and
                block_hash == block.compute_hash())


    def add_block(self, block, proof):
        # adding the block to the chain after verification
        """
        How does verification work?
        1. is_valid_proof
        2. the previous hash is referred in the block and hash of a latest block in the chain match.
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not BlockC.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True


    @property
    def last_block(self):
        return self.chain[-1]
