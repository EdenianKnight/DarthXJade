from solders.keypair import Keypair
from solana.rpc.api import Client
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID

# Connect to Solana Devnet
solana_client = Client("https://api.devnet.solana.com")

# Load the token authority keypair (previously generated in deploy_token.py)
authority = Keypair()

def mint_deolax(deolax_token_address, recipient_address, amount):
    print(f"Minting {amount} DeolaX tokens to {recipient_address}...")
    
    # Load the token
    deolax_token = Token(solana_client, deolax_token_address, TOKEN_PROGRAM_ID, authority)
    
    # Get or create the recipient's associated token account
    recipient_token_account = deolax_token.get_or_create_associated_account_info(recipient_address)
    
    # Mint tokens
    deolax_token.mint_to(recipient_token_account.address, authority, amount)
    
    print(f"Successfully minted {amount} DeolaX tokens to {recipient_address}")

if __name__ == "__main__":
    # Example usage (Replace with actual token and recipient addresses)
    mint_deolax("BJqc3irWUJzELUHyVEtNqkVwJ71aysjnCQpT5xMoHcGR", "5YRTtA6uR1vxQ67jQDTNzDUgkRSpwvvvshUBveDdKeH8", 1000)
