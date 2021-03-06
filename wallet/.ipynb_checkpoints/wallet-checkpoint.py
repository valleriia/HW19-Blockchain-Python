# Import dependencies
import subprocess
import json
from dotenv import load_dotenv

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("MNEM")

# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE
#./derive --key=xprv9zbB6Xchu2zRkf6jSEnH9vuy7tpBuq2njDRr9efSGBXSYr1QtN8QHRur28QLQvKRqFThCxopdS1UD61a5q6jGyuJPGLDV9XfYHQto72DAE8 --cols=path,address --coin=ZEC --numderive=3 -g
coin="ZEC"
numderive=3
format="json"
 
# Create a function called `derive_wallets`
def derive_wallets():
    command = "./derive --key=mnemonic --cols=path,address --coin=coin --numderive=numderive -g"
    print(command)
    #p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    #output, err = p.communicate()
    #p_status = p.wait()
    #return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = # YOUR CODE HERE

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(# YOUR CODE HERE):
    # YOUR CODE HERE
    

derive_wallets()

