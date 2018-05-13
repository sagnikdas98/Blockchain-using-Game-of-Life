import json
import time


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = []
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self):
        return


class Blockchain:

    def __init__(self):
        self.unconfirmed_transactions = [ ]  # data yet to get into blockchain
        self.chain = [ ]
        self.create_genesis_block ()

    def create_genesis_block(self):
        genesis_block = Block (0 , [ ] , time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash ()
        self.chain.append (genesis_block)

    @property
    def last_block(self):
        return self.chain[ -1]