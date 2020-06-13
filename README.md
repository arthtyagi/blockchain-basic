# blockchain-basic
This is a basic blockchain app in Python for fun. Not really scalable or anything but I had fun, yo!
P.S This app doesn't have an interface, feel free to create one yourself, I'll do the whole interface thing with the second project on Blockchain whenever I do one, maybe next weekend.

Will move on to a more complex project once I'm done with this probably with Ether.js

I read [this guide](https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/) to understand how Blockchain works right down to the core ( I'm mostly only familiar with implementing smart contracts, that's just basic stuff ) and implement a Python with an interface using the microframework, Flask.

#### Step Zero : Learn more about blockchain [here](https://bitcoin.org/bitcoin.pdf) and have a good understanding of Python and REST APIs.

* 1.  Store transactions into blocks
* 2.  Add digital fingerprints to the blocks
* 3.  Chain the blocks
* 4.  Implement a proof of work algorithm
* 5.  Add blocks to the chain
* 6.  Create interfaces
* 7.  Establish consensus and decentralization
* 8.  Build the application
* 9.  Run the application

- Alright so well in a nutshell, how would you define a blockchain? 

I suppose it'd be fair to assume after reading the paper on Bitcoin by Satoshi Nakamoto that Blockchain is essentially a chain of blocks that only have an append function with a few rules that define how an append function is used.

To elucidate it a bit more, it is basically a decentralized way of storing data with blocks of cryptographic hashes that are linked to each other.

With that out of the way, let's talk about the rules that apply to appending data in a blockchain.
 
This thing is starting out as a small project for me but if I actually get hooked on this, then I guess I'll go more in-depth and learn more about blockchain and start using better services but most of all, always get the basics fuckin strong, yo!!

From [this great guide by a contributor for developer.ibm.com](https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/) to get started with blockchain :
All of the magic lies in the way this data is stored and added to the blockchain. A blockchain is essentially a linked list that contains ordered data, with a few constraints such as:

- Blocks can’t be modified once added; in other words, it is append only.
- There are specific rules for appending data to it.
- Its architecture is distributed.

 *Enforcing these constraints yields the following benefits:*

- Immutability and durability of data
- No single point of control or failure
- A verifiable audit trail of the order in which data was added. 

## Moving on to understanding how this would all tie in together :



