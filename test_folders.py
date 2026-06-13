#!/usr/bin/env python3
"""
Secure File Encryption System - Folder Structure & Initialization Test
Verifies that all folders (src/, output/, keys/) are created and working correctly
"""
import os
import sys
from pathlib import Path

def check_folder_structure():
    """Check and create folder structure"""
    print("=" * 70)
    print("🔍 FOLDER STRUCTURE VERIFICATION")
    print("=" * 70)
    
    project_root = Path(__file__).parent
    folders_to_check = {
        'src': project_root / 'src',
        'output': project_root / 'output',
        'keys': project_root / 'keys',
        'data': project_root / 'data'
    }
    
    print(f"\n📍 Project Root: {project_root}\n")
    
    all_good = True
    for folder_name, folder_path in folders_to_check.items():
        if folder_path.exists():
            print(f"✅ {folder_name:15} → EXISTS at {folder_path}")
            # Check if writable
            try:
                test_file = folder_path / '.test_write'
                test_file.touch()
                test_file.unlink()
                print(f"   ✓ Writable: YES")
            except Exception as e:
                print(f"   ✗ Writable: NO - {e}")
                all_good = False
        else:
            print(f"⚠️  {folder_name:15} → MISSING - Creating...")
            try:
                folder_path.mkdir(parents=True, exist_ok=True)
                print(f"   ✓ Created successfully!")
            except Exception as e:
                print(f"   ✗ Failed to create: {e}")
                all_good = False
    
    return all_good

def check_python_files():
    """Check if all required Python files exist"""
    print("\n" + "=" * 70)
    print("📄 PYTHON FILES VERIFICATION")
    print("=" * 70 + "\n")
    
    project_root = Path(__file__).parent
    required_files = {
        'main.py': project_root / 'main.py',
        'requirements.txt': project_root / 'requirements.txt',
        'src/__init__.py': project_root / 'src' / '__init__.py',
        'src/encryptor.py': project_root / 'src' / 'encryptor.py',
        'src/gui.py': project_root / 'src' / 'gui.py',
        'src/key_manager.py': project_root / 'src' / 'key_manager.py',
    }
    
    all_found = True
    for file_name, file_path in required_files.items():
        if file_path.exists():
            size = os.path.getsize(file_path)
            print(f"✅ {file_name:25} → EXISTS ({size} bytes)")
        else:
            print(f"❌ {file_name:25} → MISSING")
            all_found = False
    
    return all_found

def check_imports():
    """Test if core modules can be imported"""
    print("\n" + "=" * 70)
    print("🔗 IMPORT VERIFICATION")
    print("=" * 70 + "\n")
    
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))
    
    imports_to_test = {
        'cryptography': False,
        'src.encryptor': False,
        'src.key_manager': False,
    }
    
    all_imported = True
    
    # Test cryptography module
    try:
        import cryptography
        print(f"✅ cryptography module      → IMPORTED")
        imports_to_test['cryptography'] = True
    except ImportError as e:
        print(f"❌ cryptography module      → FAILED - {e}")
        all_imported = False
    
    # Test src.encryptor
    try:
        from src.encryptor import FileEncryptor
        print(f"✅ src.encryptor            → IMPORTED (FileEncryptor class found)")
        imports_to_test['src.encryptor'] = True
    except Exception as e:
        print(f"❌ src.encryptor            → FAILED - {e}")
        all_imported = False
    
    # Test src.key_manager
    try:
        from src.key_manager import KeyManager
        print(f"✅ src.key_manager          → IMPORTED (KeyManager class found)")
        imports_to_test['src.key_manager'] = True
    except Exception as e:
        print(f"❌ src.key_manager          → FAILED - {e}")
        all_imported = False
    
    return all_imported

def test_encryptor_functionality():
    """Test FileEncryptor class initialization"""
    print("\n" + "=" * 70)
    print("⚙️  ENCRYPTOR FUNCTIONALITY TEST")
    print("=" * 70 + "\n")
    
    try:
        from src.encryptor import FileEncryptor
        
        encryptor = FileEncryptor()
        print(f"✅ FileEncryptor initialized successfully")
        
        # Check directories
        print(f"   • Output directory: {encryptor.output_dir}")
        if encryptor.output_dir.exists():
            print(f"     ✓ Exists and is accessible")
        else:
            print(f"     ✗ Does not exist")
        
        print(f"   • Keys directory: {encryptor.keys_dir}")
        if encryptor.keys_dir.exists():
            print(f"     ✓ Exists and is accessible")
        else:
            print(f"     ✗ Does not exist")
        
        return True
    except Exception as e:
        print(f"❌ FileEncryptor initialization failed: {e}")
        return False

def test_key_manager_functionality():
    """Test KeyManager class initialization"""
    print("\n" + "=" * 70)
    print("🔑 KEY MANAGER FUNCTIONALITY TEST")
    print("=" * 70 + "\n")
    
    try:
        from src.key_manager import KeyManager
        
        km = KeyManager()
        print(f"✅ KeyManager initialized successfully")
        
        # Check keys directory
        print(f"   • Keys directory: {km.keys_dir}")
        if km.keys_dir.exists():
            print(f"     ✓ Exists and is accessible")
        else:
            print(f"     ✗ Does not exist")
        
        return True
    except Exception as e:
        print(f"❌ KeyManager initialization failed: {e}")
        return False

def generate_test_report():
    """Generate comprehensive test report"""
    print("\n" + "=" * 70)
    print("📊 COMPREHENSIVE TEST REPORT")
    print("=" * 70 + "\n")
    
    results = {
        'Folder Structure': check_folder_structure(),
        'Python Files': check_python_files(),
        'Imports': check_imports(),
        'Encryptor': test_encryptor_functionality(),
        'KeyManager': test_key_manager_functionality(),
    }
    
    print("\n" + "=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:25} {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 70)
    if all_passed:
        print("🎉 ALL TESTS PASSED! System is ready to use.")
        print("\nYou can now run:")
        print("  python main.py          (To start the GUI)")
        print("  python src/encryptor.py (To run encryption tests)")
        print("  python src/key_manager.py (To test key generation)")
    else:
        print("⚠️  SOME TESTS FAILED! Please fix the issues above.")
        print("\nCommon fixes:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Check folder permissions")
        print("  3. Ensure Python 3.8+ is installed")
    print("=" * 70 + "\n")
    
    return all_passed

if __name__ == "__main__":
    try:
        success = generate_test_report()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
