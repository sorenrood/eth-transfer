from web3 import Web3
import os

# setup the infura eth node (plug in your project id)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your-project-id'))

# setup addresses and get private key for address1
address1 = Web3.toChecksumAddress('your_public_address')
address2 = Web3.toChecksumAddress('receiver_public_address')
private_key = os.getenv('PRIVATE_KEY')

# in this case, the nonce is the amount of transactions on account1
nonce = w3.eth.getTransactionCount(address1)

# setup the transaction
tx = {
  'nonce': nonce,
  'to': address2,
  'value': w3.toWei(0.001, 'ether'),
  'gas': 21000,
  'gasPrice': w3.toWei(40, 'gwei'),
}

# sign the transaction with the private key from address1
signed_tx = w3.eth.account.signTransaction(tx, private_key)

# send the raw transaction to the eth node
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
