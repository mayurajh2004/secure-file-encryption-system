#!/usr/bin/env python3
"""
RSA Key Manager for Secure File Encryption System
Stores keys in the keys/ folder
"""
import os
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

class KeyManager:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.keys_dir = self.project_root / 'keys'
        self.keys_dir.mkdir(exist_ok=True)
        
        self.private_key_path = self.keys_dir / 'private_key.pem'
        self.public_key_path = self.keys_dir / 'public_key.pem'
    
    def generate_rsa_keys(self, key_size=2048):
        """Generate RSA key pair and save to keys folder"""
        print(f"🔑 Generating RSA-{key_size} key pair...")
        
        # Generate private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        
        # Save private key
        with open(self.private_key_path, 'wb') as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        
        # Save public key
        public_key = private_key.public_key()
        with open(self.public_key_path, 'wb') as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        
        # Set proper permissions (read-only for owner)
        os.chmod(self.private_key_path, 0o600)
        os.chmod(self.public_key_path, 0o644)
        
        print(f"✅ Private key saved: {self.private_key_path}")
        print(f"✅ Public key saved: {self.public_key_path}")
        
        return str(self.private_key_path), str(self.public_key_path)
    
    def load_private_key(self):
        """Load private key from keys folder"""
        with open(self.private_key_path, 'rb') as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )
        return private_key
    
    def load_public_key(self):
        """Load public key from keys folder"""
        with open(self.public_key_path, 'rb') as f:
            public_key = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )
        return public_key
    
    def list_keys(self):
        """List all keys in keys folder"""
        keys = list(self.keys_dir.glob('*.pem'))
        hash_files = list(self.keys_dir.glob('*.txt'))
        
        print("\n📁 Keys Directory Contents:")
        print("=" * 40)
        
        if keys:
            print("\n🔑 RSA Keys:")
            for key in keys:
                size = os.path.getsize(key)
                print(f"   📄 {key.name} ({size} bytes)")
        
        if hash_files:
            print("\n🔐 Hash Files:")
            for hf in hash_files:
                size = os.path.getsize(hf)
                print(f"   📄 {hf.name} ({size} bytes)")
        
        if not keys and not hash_files:
            print("   (No keys or hash files found)")

if __name__ == "__main__":
    # Test key manager
    km = KeyManager()
    
    print("Secure File Encryption - Key Manager")
    print("=" * 40)
    
    # Generate keys
    km.generate_rsa_keys()
    
    # List all keys
    km.list_keys()

