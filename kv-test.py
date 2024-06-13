from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Get environment variables from .env
from dotenv import load_dotenv
import os
load_dotenv()

# Get the Key Vault URL from the dotenv
key_vault_url = os.getenv("KEY_VAULT_URL")

# Replace with the name of your secret
secret_name = os.getenv("SECRET_NAME")

# Client ID of the managed identity used to authenticate to the Key Vault
client_id = os.getenv("CLIENT_ID")

# Get a credential to authenticate with the Key Vault
credential = DefaultAzureCredential(managed_identity_client_id=client_id)

# Create a secret client using the credential
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# Retrieve the secret
secret = secret_client.get_secret(secret_name)

print(f"The secret value is: {secret.value}")