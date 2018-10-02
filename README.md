# BurstTestnetTester

This script has some functions that make interfacing with Burst blockchain easier. It uses these functions to stress-test the Burst-testnet with regular/multi-out/multi-out-same transactions with a default 3s delay.

To use, simply execute the tester.py file (python tester.py). It will load the accounts defined in the .pkl file and start sending transactions between them. This file contains 4096 testnet accounts with ~100 Burst each. The passwords for these accounts are 'test0','test1','test2'...etc. 

Sometimes you will see JSON decoding errors, this is because the testnet server failed to process the transaction.
