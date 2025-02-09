from solana.rpc.api import Client
from solders.transaction import Transaction
from solders.keypair import Keypair
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID

# Connect to Solana Devnet
device = "https://api.devnet.solana.com"
solana_client = Client(device)

# Generate a new keypair for the token authority
authority = Keypair()

# Create DeolaX Token
def create_deolax_token():
    print("Creating DeolaX token...")
    deolax_token = Token.create_mint(
        solana_client,
        authority,
        authority.public_key,
        6,  # Decimals
        TOKEN_PROGRAM_ID
    )
    print(f"DeolaX Token Address: {deolax_token.pubkey}")
    return deolax_token

if __name__ == "__main__":
    create_deolax_token()
