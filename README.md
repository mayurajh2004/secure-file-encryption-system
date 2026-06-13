# Secure File Encryption System

A robust, production-ready Python-based file encryption system designed to provide advanced security features for protecting sensitive data at rest. This system implements industry-standard cryptographic algorithms to ensure data confidentiality and integrity.

![Secure File Encryption System GUI](https://raw.githubusercontent.com/mayurajh2004/secure-file-encryption-system/main/docs/gui_screenshot.png)

## 🔐 Features

- **AES-256 Encryption**: Implements AES-256 encryption for maximum security
- **SHA-256 Integrity Verification**: Built-in integrity checks using SHA-256 hashing
- **Tamper Detection**: Advanced tamper detection mechanisms
- **User-Friendly GUI Interface**: Modern, intuitive graphical interface for easy file encryption/decryption
- **Password-Based Protection**: Strong password-based encryption support
- **Cross-Platform Support**: Works seamlessly on Windows, macOS, and Linux
- **Operation Logging**: Comprehensive operation logs for audit trails
- **Performance Optimized**: Efficient encryption for files of all sizes
- **Error Handling**: Comprehensive error handling and validation

## 📋 System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Linux, macOS, or Windows
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk Space**: At least 500MB for installation and operations

## 🐧 Linux Installation Guide

### Step 1: Update System Packages

```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install Python and pip

```bash
sudo apt install -y python3 python3-pip python3-venv
```

### Step 3: Install Required System Dependencies

```bash
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

For GUI support, also install:

```bash
sudo apt install -y python3-tk python3-dev
```

### Step 4: Clone the Repository

```bash
git clone https://github.com/mayurajh2004/secure-file-encryption-system.git
cd secure-file-encryption-system
```

### Step 5: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 6: Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Typical requirements.txt contents:

```
cryptography>=41.0.0
pycryptodome>=3.18.0
```

## 🚀 Quick Start

### Running the GUI Application

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run the application
python main.py
```

The GUI window will open with the following interface elements:

- **File Selection**: Browse and select files to encrypt/decrypt
- **Password Field**: Enter a strong password for encryption
- **Integrity Check**: Compute SHA-256 hash for file verification
- **Encrypt/Decrypt Buttons**: Perform encryption or decryption operations
- **Operation Log**: View all performed operations with timestamps

### Using the GUI

1. **Encrypt a File**:
   - Click the **BROWSE** button to select a file
   - Enter a strong password in the password field
   - Click the **ENCRYPT FILE** button
   - The encrypted file will be saved in the output directory
   - Check the **OPERATION LOG** for confirmation

2. **Decrypt a File**:
   - Click the **BROWSE** button to select an encrypted file
   - Enter the same password used during encryption
   - Click the **DECRYPT FILE** button
   - The decrypted file will be saved in the output directory

3. **Verify File Integrity**:
   - Select a file using the **BROWSE** button
   - Click the **COMPUTE HASH** button
   - The SHA-256 hash will be displayed and saved to the log

### Command Line Usage

```bash
# Activate virtual environment first
source venv/bin/activate

# Encrypt a file
python main.py encrypt --input myfile.txt --output myfile.enc --password mypassword

# Decrypt a file
python main.py decrypt --input myfile.enc --output myfile.txt --password mypassword

# Compute file hash
python main.py hash --input myfile.txt
```

## 📁 Project Structure

```
secure-file-encryption-system/
├── src/
│   ├── __init__.py
│   ├── encryptor.py          # Core encryption logic
│   ├── key_manager.py         # Key generation and management
│   ├── gui.py                 # GUI implementation
│   └── utils.py               # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_encryption.py     # Encryption tests
│   └── test_integrity.py      # Integrity check tests
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── LICENSE                     # License information
├── README.md                   # This file
└── docs/
    └── gui_screenshot.png      # GUI preview
```

## 🔑 Key Features Explained

### AES-256 Encryption
- Military-grade encryption standard
- 256-bit key length for maximum security
- Protects data confidentiality

### SHA-256 Integrity Check
- Verifies file hasn't been tampered with
- Creates unique hash for each file
- Ensures data integrity

### Tamper Detection
- Automatically detects unauthorized modifications
- Alerts user to potential security breaches
- Prevents use of corrupted encrypted files

## 🔒 Security Best Practices

✅ **Do's**:
- Use strong, unique passwords (minimum 12 characters)
- Include uppercase, lowercase, numbers, and symbols in passwords
- Regularly backup important files before encryption
- Keep the application and Python packages updated
- Use on trusted, secure computers

❌ **Don'ts**:
- Never share passwords unencrypted
- Don't forget your encryption password
- Avoid using weak or common passwords
- Don't store passwords in plain text files
- Never use the same password for multiple sensitive files

## 🧪 Testing

Run the test suite to verify everything is working:

```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ --cov=src --cov-report=html
```

## 📊 GUI Interface Overview

The application provides a sleek, dark-themed interface with:

- **File Selection Area**: Browse and select files
- **Password Field**: Secure password input with show/hide option
- **Integrity Check Section**: SHA-256 hash computation
- **Action Buttons**: 
  - 🔐 ENCRYPT FILE (Blue)
  - 🔓 DECRYPT FILE (Pink)
  - 🗑️ CLEAR ALL (Gray)
- **Operation Log**: Real-time logging of all operations with timestamps
- **Progress Bar**: Visual feedback during encryption/decryption

## ⚙️ Advanced Configuration

### Custom Output Directory

Edit the configuration in `src/utils.py`:

```python
OUTPUT_DIRECTORY = "/home/user/encrypted_files"
```

### Password Requirements

Modify password strength requirements in `src/key_manager.py`:

```python
MIN_PASSWORD_LENGTH = 12
REQUIRE_SPECIAL_CHARS = True
```

## 🚨 Troubleshooting

### Issue: "Module not found" error

**Solution**: Ensure virtual environment is activated:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: GUI won't open

**Solution**: Install tkinter for your Linux distribution:
```bash
sudo apt install python3-tk
```

### Issue: Permission denied errors

**Solution**: Check file permissions:
```bash
chmod 755 main.py
chmod 755 -R src/
```

### Issue: "Cryptography module not found"

**Solution**: Reinstall cryptography with build tools:
```bash
pip install --upgrade --force-reinstall cryptography
```

## 📚 Documentation

For API reference and advanced usage examples, check the inline code documentation:

```bash
python -c "import src.encryptor; help(src.encryptor.Encryptor)"
```

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

The authors assume no liability for data loss or damages resulting from the use of this software.

## 🆘 Common Commands Reference

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run application
python main.py

# Run tests
python -m pytest tests/ -v

# Deactivate virtual environment
deactivate

# Clean up Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```

## 📧 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/mayurajh2004/secure-file-encryption-system/issues)
- Check existing documentation
- Review the operation logs for error details

## 👨‍💻 Author

**Mayuraj H**
- GitHub: [@mayurajh2004](https://github.com/mayurajh2004)
- Repository: [secure-file-encryption-system](https://github.com/mayurajh2004/secure-file-encryption-system)

---

**Last Updated**: June 2026  
**Version**: 1.0.0  
**Status**: Active & Maintained
