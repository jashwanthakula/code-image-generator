import secrets
import base64
secret_key = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode('utf-8')
print(secret_key)  # e.g., "c2VjcmV0X2tleV9oZXJlXzMyX2J5dGVzX2xvbg=="