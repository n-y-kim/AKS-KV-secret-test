from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Replace with your Key Vault URL
key_vault_url = "https://kv-ccq2.vault.azure.net"

# Replace with the name of your secret
secret_name = "secret"

# Get a credential to authenticate with the Key Vault
credential = DefaultAzureCredential()

# Create a secret client using the credential
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# Retrieve the secret
secret = secret_client.get_secret(secret_name)

print(f"The secret value is: {secret.value}")