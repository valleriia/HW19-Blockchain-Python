# Import dependencies
import subprocess 
import json
from dotenv import load_dotenv
from constants import *
from pprint import pprint
import os
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware
# Load and set environment variables
load_dotenv("mnemonic.env")
mnemonic=os.getenv("MNEM")
mnemonic="'"+mnemonic+"'"
numderive=3
format="json"
coin="ZEC"

# connect Web3
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
# enable PoA middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# set gas price strategy to built-in "medium" algorithm (est ~5min per tx)
# see https://web3py.readthedocs.io/en/stable/gas_price.html?highlight=gas
# see https://ethgasstation.info/ API for a more accurate strategy
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE

#./derive --key=xprv9s21ZrQH143K49v24E69FCwKpbe2MgrtifNKxsfZuLdBGXpXWeP236d5EzsCmNQBAYrAx2s94h2WFYa7vqDsD7qYMMBsWnrJEqwAseZaCbh --cols=path,address --coin=ZEC --numderive=3 -g
 
# Create a function called `derive_wallets`
def derive_wallets(coin,mnemonic=mnemonic,numderive=3):
    command = f"php ./derive --mnemonic={mnemonic} --cols=all --coin={coin} --numderive={numderive}  --format={format} -g"
    print(command)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    print(output)
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
#coins = # YOUR CODE HERE

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    # YOUR CODE HERE



# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def create_tx(coin,account,to,amount):
    if coin == ETH:
        value = w3.toWei(amount, "ether") # convert 1.2 ETH to 120000000000 wei
        gasEstimate = w3.eth.estimateGas({ "to": to, "from": account, "amount": value })
        return {
            "to": to,
            "from": account,
            "value": value,
            "gas": gasEstimate,
           # "gasPrice": w3.eth.generateGasPrice(),
            "gasPrice": 1,
            "nonce": w3.eth.getTransactionCount(account),
            "chainId": w3.eth.chain_id
        }
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin,account,to,amount):
    if coin == ETH:
        raw_tx = create_tx(coin, account.address, to, amount)
        signed = account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    if coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)

        
#print (derive_wallets(BTCTEST))
coins={ETH:derive_wallets(coin=ETH),BTCTEST:derive_wallets(coin=BTCTEST),}
#res1 = coins["ETH"]("ETH")
#res2 = coins["BTCTEST"] ("BTCTEST")
pprint(coins)
#print(res2)

#BTC: JSON Response, ETH: JSONRESPONSE

account = priv_key_to_account(BTCTEST, coins[BTCTEST][1]['privkey'])

#create_tx(BTCTEST, account, 'mqPU33vMnMtgyXYYpwT1szR8GDr8dig3HT', 0.001)

#send_tx(BTCTEST, account, 'mosMyxViFa2g2k1xK3EGxVGRPjVecEyNZB', 0.001)

account = priv_key_to_account(ETH, coins[ETH][1]['privkey'])

send_tx(ETH, account, '0xD192F42eE6CF1f476E51Df754e3Ce3aeAA458290', 124)