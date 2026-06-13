#!/usr/bin/env python3
"""
Secure File Encryption System - Main Entry Point
Launches the GUI application
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.gui import EncryptionGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = EncryptionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
