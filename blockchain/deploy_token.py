from solana.rpc.api import Client
from solders.transaction import Transaction
from solders.keypair import Keypair
from spl.token.core import create_mint  # Updated import
from spl.token.constants import TOKEN_PROGRAM_ID

# Connect to Solana Devnet
device = "https://api.devnet.solana.com"
solana_client = Client(device)

# Generate a new keypair for the token authority
authority = Keypair()

# Create DeolaX Token
def create_deolax_token():
    print("Creating DeolaX token...")

    # Create the token mint
    deolax_token = create_mint(
        solana_client,
        authority,  # Payer
        authority.pubkey(),  # Mint authority
        authority.pubkey(),  # Freeze authority
        6,  # Decimals
    )

    print(f"DeolaX Token Address: {deolax_token}")
    return deolax_token

if __name__ == "__main__":
    create_deolax_token()