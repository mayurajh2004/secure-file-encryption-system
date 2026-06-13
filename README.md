# Secure File Encryption System

A robust, production-ready Python-based file encryption system designed to provide advanced security features for protecting sensitive data at rest. This system implements industry-standard cryptography with AES-256 encryption and SHA-256 integrity verification.

![Secure File Encryption System GUI](https://raw.githubusercontent.com/mayurajh2004/secure-file-encryption-system/main/docs/gui_screenshot.png)

## 🔐 Features

- **AES-256 Encryption**: Military-grade encryption standard with 256-bit key length
- **SHA-256 Integrity Verification**: Built-in integrity checks using SHA-256 hashing
- **Tamper Detection**: Automatically detects unauthorized modifications and file corruption
- **User-Friendly GUI Interface**: Modern, dark-themed graphical interface for easy encryption/decryption
- **Password-Based Protection**: Strong password-based encryption support (PBKDF2 key derivation)
- **Cross-Platform Support**: Works seamlessly on Windows, macOS, and Linux
- **Operation Logging**: Comprehensive operation logs with timestamps for audit trails
- **Performance Optimized**: Efficient encryption for files of all sizes
- **Error Handling**: Comprehensive error handling and validation
- **Automatic Folder Creation**: Automatically creates output/, keys/, and data/ directories

## 📋 System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Linux, macOS, or Windows
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk Space**: At least 500MB for installation and operations
- **GUI Support**: tkinter (usually pre-installed with Python)

## 🚀 Quick Start (5 Minutes)

### Step 1: Clone the Repository

```bash
git clone https://github.com/mayurajh2004/secure-file-encryption-system.git
cd secure-file-encryption-system
```

### Step 2: Create Virtual Environment

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python test_folders.py
```

This will check all folders, Python files, and verify that the encryption system is working correctly.

### Step 5: Run the Application

```bash
python main.py
```

The GUI window will open with the following features:

- **📂 File Selection**: Browse and select any file to encrypt/decrypt
- **🔑 Password Field**: Enter a strong password with show/hide option
- **🔐 ENCRYPT FILE**: Encrypt files with AES-256 encryption
- **🔓 DECRYPT FILE**: Decrypt .enc files with integrity verification
- **✅ COMPUTE HASH**: Verify file integrity with SHA-256
- **📋 OPERATION LOG**: Real-time logging of all operations
- **⏳ Progress Bar**: Visual feedback during encryption/decryption

## 📁 Project Structure

```
secure-file-encryption-system/
├── src/
│   ├── __init__.py              # Package initialization
│   ├── encryptor.py             # Core AES-256 encryption logic
│   ├── gui.py                   # Professional GUI implementation
│   └── key_manager.py           # RSA key generation and management
├── output/                      # Auto-created: Encrypted files saved here
├── keys/                        # Auto-created: Encryption keys & hashes saved here
├── data/                        # Auto-created: Test files directory
├── main.py                      # Application entry point (GUI launcher)
├── test_folders.py              # System verification and testing script
├── requirements.txt             # Python dependencies (cryptography, pycryptodome)
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## 🔐 How to Use the GUI

### 1. **Encrypt a File**
   - Click the **📂 BROWSE** button to select a file
   - Enter a strong password in the **🔑 PASSWORD** field
   - Click the **🔒 ENCRYPT FILE** button
   - The encrypted file will be saved in the `output/` folder
   - A hash file will be saved in the `keys/` folder
   - Check the **📋 OPERATION LOG** for confirmation

### 2. **Decrypt a File**
   - Click the **📂 BROWSE** button to select an encrypted file (`.enc`)
   - Enter the **exact same password** used during encryption
   - Click the **🔓 DECRYPT FILE** button
   - The system will verify file integrity automatically
   - If tampering is detected, you'll receive an alert
   - The decrypted file will be saved in the `output/` folder

### 3. **Verify File Integrity**
   - Select any file using the **📂 BROWSE** button
   - The **SHA-256 hash** will be automatically computed
   - Click **✅ COMPUTE HASH** for full hash display
   - Use the hash to verify file integrity later

## ⚙️ Command Line Usage

### Test the Encryption System
```bash
python src/encryptor.py
```
This will:
- Create a test file in `data/` folder
- Encrypt it with a sample password
- Decrypt it and verify integrity
- Show all operations in the console

### Generate RSA Keys
```bash
python src/key_manager.py
```
This will:
- Generate RSA-2048 key pair
- Save private key to `keys/private_key.pem`
- Save public key to `keys/public_key.pem`

## 🔑 Key Features Explained

### AES-256 Encryption
- Military-grade encryption standard (NIST approved)
- 256-bit key length for maximum security
- PBKDF2 key derivation (100,000 iterations)
- CBC mode with random IV for each file
- Protects data confidentiality

### SHA-256 Integrity Check
- Verifies file hasn't been tampered with
- Creates unique hash for each file
- Stored with encrypted file
- Automatically verified during decryption
- Ensures data integrity

### Tamper Detection
- Automatically detects unauthorized modifications
- Compares stored hash with computed hash during decryption
- Alerts user to potential security breaches
- Prevents use of corrupted encrypted files

## 🔒 Security Best Practices

✅ **Do's**:
- Use strong, unique passwords (minimum 12 characters)
- Include uppercase, lowercase, numbers, and symbols in passwords
- Regularly backup important files before encryption
- Keep the application and Python packages updated
- Use on trusted, secure computers
- Remember your encryption password (it cannot be recovered)

❌ **Don'ts**:
- Never share passwords unencrypted
- Don't forget your encryption password
- Avoid using weak or common passwords
- Don't store passwords in plain text files
- Never use the same password for multiple sensitive files
- Don't modify encrypted files manually

## 🧪 Testing

### Verify System Installation
```bash
python test_folders.py
```

Expected output:
```
✅ Folder Structure            PASS
✅ Python Files                PASS
✅ Imports                     PASS
✅ Encryptor                   PASS
✅ KeyManager                  PASS

🎉 ALL TESTS PASSED! System is ready to use.
```

### Test Encryption/Decryption
```bash
python src/encryptor.py
```

## 📊 GUI Interface Overview

The application provides a professional, dark-themed interface with:

- **🎨 Modern Design**: Dark theme with color-coded sections
- **📁 File Selection Area**: Browse and select files with visual feedback
- **🔑 Password Field**: Secure password input with show/hide option
- **🔐 Integrity Check Section**: SHA-256 hash computation and display
- **🔘 Action Buttons**: 
  - 🔒 ENCRYPT FILE (Blue)
  - 🔓 DECRYPT FILE (Pink)
  - 🗑️ CLEAR ALL (Gray)
- **📋 Operation Log**: Real-time logging with timestamps and color coding
- **⏳ Progress Bar**: Visual feedback during encryption/decryption
- **📊 Status Bar**: Shows current operation status

## 🚨 Troubleshooting

### Issue: "Module not found" error
**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: GUI won't open
**Solution**: Install tkinter for your system:
```bash
# Linux (Debian/Ubuntu)
sudo apt install python3-tk

# Linux (Fedora/RHEL)
sudo dnf install python3-tkinter

# macOS
brew install python-tk@3.9

# Windows: Reinstall Python with "tcl/tk and IDLE" option checked
```

### Issue: Permission denied errors
**Solution**: Check and fix file permissions:
```bash
chmod +x main.py
chmod -R 755 src/
chmod -R 755 output/
```

### Issue: "Cryptography module not found"
**Solution**: Reinstall cryptography with build tools:
```bash
pip install --upgrade --force-reinstall cryptography
```

### Issue: Encrypted files not appearing in output/
**Solution**: Check that the output/ folder exists and is writable:
```bash
python test_folders.py
```

## 📚 Documentation

### API Reference
For inline code documentation:
```bash
python -c "import src.encryptor; help(src.encryptor.FileEncryptor)"
python -c "import src.key_manager; help(src.key_manager.KeyManager)"
```

### File Structure
- `src/encryptor.py`: Contains `FileEncryptor` class with encryption/decryption methods
- `src/gui.py`: Contains `EncryptionGUI` class for the GUI interface
- `src/key_manager.py`: Contains `KeyManager` class for RSA key management

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## ⚖️ Disclaimer

This software is provided "as is" without warranty of any kind. Users are responsible for:
- Maintaining secure backups of original files
- Remembering encryption passwords
- Ensuring compliance with applicable laws and regulations regarding encryption
- Regular security updates and maintenance
- Testing the software with non-critical files first

The authors assume no liability for data loss or damages resulting from the use of this software.

## 🆘 Common Commands Reference

```bash
# ===== SETUP =====
python3 -m venv venv
source venv/bin/activate              # Linux/macOS
venv\Scripts\activate                 # Windows
pip install -r requirements.txt

# ===== RUN APPLICATION =====
python main.py                        # Start GUI

# ===== TESTING =====
python test_folders.py                # Verify installation
python src/encryptor.py               # Test encryption
python src/key_manager.py             # Test key generation

# ===== CLEANUP =====
deactivate                            # Exit virtual environment
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```
<img width="456" height="384" alt="image" src="https://github.com/user-attachments/assets/e47c4cf5-331c-4cde-9358-8eec1e898ea4" />


## 📧 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/mayurajh2004/secure-file-encryption-system/issues)
- Check existing documentation in this README
- Review the operation logs in the GUI for error details
- Run `python test_folders.py` to diagnose system issues

## 👨‍💻 Author

**Mayuraj H**
- GitHub: [@mayurajh2004](https://github.com/mayurajh2004)
- Repository: [secure-file-encryption-system](https://github.com/mayurajh2004/secure-file-encryption-system)

---

**Last Updated**: June 2026  
**Version**: 1.0.0  
**Status**: Active & Maintained ✅  
**Tested On**: Windows 10+, Ubuntu 20.04+, macOS 10.15+
