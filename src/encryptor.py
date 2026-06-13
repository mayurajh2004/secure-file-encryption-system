#!/usr/bin/env python3
"""
Secure File Encryption System
AES-256 Encryption with SHA-256 Integrity Verification
Files saved to proper folders: output/ for encrypted, keys/ for hashes
"""
import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from datetime import datetime
from pathlib import Path

class FileEncryptor:
    """Handles AES-256 file encryption and decryption"""
    
    def __init__(self):
        self.backend = default_backend()
        # Get the project root directory
        self.project_root = Path(__file__).parent.parent
        self.output_dir = self.project_root / 'output'
        self.keys_dir = self.project_root / 'keys'
        
        # Create directories if they don't exist
        self.output_dir.mkdir(exist_ok=True)
        self.keys_dir.mkdir(exist_ok=True)
    
    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive AES-256 key from password using PBKDF2"""
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000,  # 100,000 iterations for security
            dklen=32  # 32 bytes = AES-256
        )
    
    def encrypt_file(self, file_path: str, password: str, output_path: str = None):
        """
        Encrypt a file using AES-256-CBC
        Saves: salt + IV + hash + ciphertext
        """
        # Generate random salt and IV
        salt = os.urandom(16)
        iv = os.urandom(16)
        
        # Derive encryption key
        key = self._derive_key(password, salt)
        
        # Read original file
        with open(file_path, 'rb') as f:
            plaintext = f.read()
        
        # Compute SHA-256 hash for integrity
        file_hash = hashlib.sha256(plaintext).hexdigest()
        
        # Pad data to AES block size (16 bytes)
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()
        
        # Encrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # Package: salt(16) + iv(16) + hash_len(2) + hash(64) + ciphertext
        hash_bytes = file_hash.encode('utf-8')
        hash_len = len(hash_bytes).to_bytes(2, 'big')
        
        output_data = salt + iv + hash_len + hash_bytes + ciphertext
        
        # Save encrypted file
        if output_path is None:
            # Save to output folder with original filename
            original_name = Path(file_path).stem
            output_path = self.output_dir / f"{original_name}_encrypted.enc"
        else:
            output_path = Path(output_path)
        
        # Ensure output_path is in output directory
        if output_path.parent != self.output_dir:
            output_path = self.output_dir / output_path.name
        
        with open(output_path, 'wb') as f:
            f.write(output_data)
        
        # Save hash file in keys folder (not alongside original)
        hash_filename = f"{Path(file_path).stem}_hash.txt"
        hash_path = self.keys_dir / hash_filename
        
        with open(hash_path, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("SECURE FILE ENCRYPTION SYSTEM - INTEGRITY HASH\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Original File: {Path(file_path).name}\n")
            f.write(f"Encrypted File: {output_path.name}\n")
            f.write(f"Date Encrypted: {datetime.now()}\n\n")
            f.write(f"SHA-256 HASH: {file_hash}\n\n")
            f.write("=" * 60 + "\n")
            f.write("⚠️ IMPORTANT: Use this hash to verify file integrity\n")
            f.write("=" * 60 + "\n")
        
        print(f"✅ Encrypted: {output_path}")
        print(f"🔑 Hash saved: {hash_path}")
        print(f"🔐 SHA-256: {file_hash[:32]}...")
        
        return str(output_path)
    
    def decrypt_file(self, file_path: str, password: str, output_path: str = None):
        """
        Decrypt a file and verify integrity
        Raises exception if tampering detected
        """
        # Read encrypted file
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        # Extract components
        salt = encrypted_data[0:16]
        iv = encrypted_data[16:32]
        hash_len = int.from_bytes(encrypted_data[32:34], 'big')
        expected_hash = encrypted_data[34:34+hash_len].decode('utf-8')
        ciphertext = encrypted_data[34+hash_len:]
        
        # Derive key
        key = self._derive_key(password, salt)
        
        # Decrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
        
        # Verify integrity
        actual_hash = hashlib.sha256(plaintext).hexdigest()
        
        if actual_hash != expected_hash:
            raise Exception(
                f"⚠️ INTEGRITY CHECK FAILED!\n"
                f"   Expected: {expected_hash}\n"
                f"   Got: {actual_hash}\n"
                f"   File may be corrupted or tampered with!"
            )
        
        # Save decrypted file to output folder
        if output_path is None:
            original_name = Path(file_path).stem
            # Remove _encrypted suffix if present
            clean_name = original_name.replace('_encrypted', '')
            output_path = self.output_dir / f"{clean_name}_decrypted.txt"
        else:
            output_path = Path(output_path)
        
        # Ensure output_path is in output directory
        if output_path.parent != self.output_dir:
            output_path = self.output_dir / output_path.name
        
        with open(output_path, 'wb') as f:
            f.write(plaintext)
        
        print(f"✅ Decrypted: {output_path}")
        print(f"✓ Integrity Check: PASSED")
        
        return str(output_path)

# Test the module
if __name__ == "__main__":
    print("=" * 50)
    print("Secure File Encryption System - Test")
    print("=" * 50)
    
    # Create test file
    test_content = """This is my secret project for the Cyber Security internship.
    AES-256 encryption provides confidentiality.
    SHA-256 hashing ensures integrity.
    The CIA triad in action!"""
    
    test_file = Path("data/test_secret.txt")
    test_file.parent.mkdir(exist_ok=True)
    
    with open(test_file, "w") as f:
        f.write(test_content)
    
    print(f"\n📄 Original file created: {test_file}")
    
    # Initialize encryptor
    encryptor = FileEncryptor()
    
    # Test encryption
    print("\n🔒 Encrypting...")
    encrypted = encryptor.encrypt_file(str(test_file), "MySecurePass123!")
    
    # Test decryption
    print("\n🔓 Decrypting...")
    decrypted = encryptor.decrypt_file(encrypted, "MySecurePass123!")
    
    # Verify content matches
    with open(test_file, 'r') as f1, open(decrypted, 'r') as f2:
        if f1.read() == f2.read():
            print("\n✅ FINAL VERIFICATION: Content matches perfectly!")
        else:
            print("\n❌ Verification failed!")
    
    print("\n" + "=" * 50)
    print("🎉 All tests passed! System is ready.")
    print("=" * 50)
    print(f"\n📁 Check these folders:")
    print(f"   Output files: {encryptor.output_dir}")
    print(f"   Key/Hash files: {encryptor.keys_dir}")


