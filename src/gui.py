#!/usr/bin/env python3
"""
Secure File Encryption System - Professional GUI
Fixed: Standard dialogs, proper error handling, clean UI
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
import hashlib
import threading
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.encryptor import FileEncryptor

class EncryptionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Secure File Encryption System")
        self.root.geometry("900x750")
        self.root.resizable(True, True)
        
        # Set color scheme
        self.colors = {
            'bg': '#1e1e2e',
            'fg': '#cdd6f4',
            'accent': '#313244',
            'success': '#a6e3a1',
            'error': '#f38ba8',
            'warning': '#f9e2af',
            'info': '#89b4fa',
            'button_encrypt': '#89b4fa',
            'button_decrypt': '#f38ba8',
            'button_browse': '#cba6f7'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        self.encryptor = FileEncryptor()
        self.selected_file = None
        self.output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Create all UI elements"""
        
        # Main container with padding
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Title Section
        self.create_title_section(main_container)
        
        # File Selection Section
        self.create_file_section(main_container)
        
        # Password Section
        self.create_password_section(main_container)
        
        # Integrity Section
        self.create_integrity_section(main_container)
        
        # Action Buttons Section
        self.create_action_buttons(main_container)
        
        # Progress Bar
        self.create_progress_bar(main_container)
        
        # Log Section
        self.create_log_section(main_container)
        
        # Status Bar
        self.create_status_bar()
        
        # Initial log
        self.log("🔐 Secure File Encryption System Ready", "INFO")
        self.log("📁 Output directory: " + self.output_dir, "INFO")
    
    def create_title_section(self, parent):
        """Create title and header"""
        title_frame = tk.Frame(parent, bg=self.colors['bg'])
        title_frame.pack(fill='x', pady=(0, 10))
        
        title_label = tk.Label(
            title_frame, 
            text="🔒 SECURE FILE ENCRYPTION SYSTEM", 
            font=("Arial", 20, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['success']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="AES-256 Encryption | SHA-256 Integrity | Tamper Detection",
            font=("Arial", 11),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        subtitle_label.pack()
        
        separator = ttk.Separator(parent, orient='horizontal')
        separator.pack(fill='x', pady=10)
    
    def create_file_section(self, parent):
        """Create file selection area"""
        file_frame = tk.LabelFrame(
            parent, 
            text="📁 FILE SELECTION", 
            bg=self.colors['bg'],
            fg=self.colors['info'],
            font=("Arial", 11, "bold"),
            relief=tk.RIDGE
        )
        file_frame.pack(fill='x', pady=10)
        
        self.file_path_var = tk.StringVar(value="No file selected")
        file_label = tk.Label(
            file_frame,
            textvariable=self.file_path_var,
            bg=self.colors['accent'],
            fg=self.colors['fg'],
            wraplength=600,
            cursor="hand2",
            font=("Arial", 10),
            relief=tk.SUNKEN,
            padx=10,
            pady=5
        )
        file_label.pack(side='left', padx=10, pady=10, fill='x', expand=True)
        
        browse_btn = tk.Button(
            file_frame,
            text="📂 BROWSE",
            command=self.select_file,
            bg=self.colors['button_browse'],
            fg='#1e1e2e',
            padx=20,
            pady=5,
            cursor="hand2",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED
        )
        browse_btn.pack(side='right', padx=10, pady=10)
    
    def create_password_section(self, parent):
        """Create password entry"""
        pass_frame = tk.LabelFrame(
            parent,
            text="🔑 PASSWORD",
            bg=self.colors['bg'],
            fg=self.colors['info'],
            font=("Arial", 11, "bold"),
            relief=tk.RIDGE
        )
        pass_frame.pack(fill='x', pady=10)
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            pass_frame,
            textvariable=self.password_var,
            show="•",
            font=("Arial", 12),
            bg=self.colors['accent'],
            fg=self.colors['fg'],
            relief=tk.SUNKEN
        )
        self.password_entry.pack(side='left', padx=10, pady=10, fill='x', expand=True)
        
        self.show_password = tk.BooleanVar(value=False)
        show_btn = tk.Button(
            pass_frame,
            text="👁 SHOW",
            command=self.toggle_password,
            bg=self.colors['info'],
            fg='#1e1e2e',
            padx=15,
            pady=5,
            cursor="hand2",
            font=("Arial", 9, "bold")
        )
        show_btn.pack(side='right', padx=5, pady=10)
        
        clear_pass_btn = tk.Button(
            pass_frame,
            text="🗑 CLEAR",
            command=self.clear_password,
            bg='#6c7086',
            fg='white',
            padx=15,
            pady=5,
            cursor="hand2",
            font=("Arial", 9, "bold")
        )
        clear_pass_btn.pack(side='right', padx=5, pady=10)
    
    def create_integrity_section(self, parent):
        """Create hash verification area"""
        hash_frame = tk.LabelFrame(
            parent,
            text="🔐 INTEGRITY CHECK (SHA-256)",
            bg=self.colors['bg'],
            fg=self.colors['info'],
            font=("Arial", 11, "bold"),
            relief=tk.RIDGE
        )
        hash_frame.pack(fill='x', pady=10)
        
        self.hash_var = tk.StringVar(value="Select a file to compute hash")
        hash_label = tk.Label(
            hash_frame,
            textvariable=self.hash_var,
            bg=self.colors['accent'],
            fg=self.colors['warning'],
            font=("Courier", 9),
            wraplength=700,
            relief=tk.SUNKEN,
            padx=10,
            pady=5
        )
        hash_label.pack(side='left', padx=10, pady=10, fill='x', expand=True)
        
        verify_btn = tk.Button(
            hash_frame,
            text="✅ COMPUTE HASH",
            command=self.compute_hash_manual,
            bg='#a6e3a1',
            fg='#1e1e2e',
            padx=15,
            pady=5,
            cursor="hand2",
            font=("Arial", 9, "bold")
        )
        verify_btn.pack(side='right', padx=5, pady=10)
    
    def create_action_buttons(self, parent):
        """Create main action buttons"""
        action_frame = tk.Frame(parent, bg=self.colors['bg'])
        action_frame.pack(pady=15)
        
        self.encrypt_btn = tk.Button(
            action_frame,
            text="🔒 ENCRYPT FILE",
            command=self.encrypt_file,
            bg=self.colors['button_encrypt'],
            fg='#1e1e2e',
            font=("Arial", 12, "bold"),
            padx=40,
            pady=12,
            cursor="hand2",
            relief=tk.RAISED
        )
        self.encrypt_btn.pack(side='left', padx=10)
        
        self.decrypt_btn = tk.Button(
            action_frame,
            text="🔓 DECRYPT FILE",
            command=self.decrypt_file,
            bg=self.colors['button_decrypt'],
            fg='#1e1e2e',
            font=("Arial", 12, "bold"),
            padx=40,
            pady=12,
            cursor="hand2",
            relief=tk.RAISED
        )
        self.decrypt_btn.pack(side='left', padx=10)
        
        clear_btn = tk.Button(
            action_frame,
            text="🗑 CLEAR ALL",
            command=self.clear_all,
            bg='#6c7086',
            fg='white',
            font=("Arial", 12, "bold"),
            padx=30,
            pady=12,
            cursor="hand2"
        )
        clear_btn.pack(side='left', padx=10)
    
    def create_progress_bar(self, parent):
        """Create progress bar"""
        self.progress = ttk.Progressbar(
            parent,
            mode='indeterminate',
            length=500
        )
        self.progress.pack(pady=10)
    
    def create_log_section(self, parent):
        """Create operation log area"""
        log_frame = tk.LabelFrame(
            parent,
            text="📋 OPERATION LOG",
            bg=self.colors['bg'],
            fg=self.colors['info'],
            font=("Arial", 11, "bold"),
            relief=tk.RIDGE
        )
        log_frame.pack(fill='both', expand=True, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=12,
            bg='#11111b',
            fg='#cdd6f4',
            font=("Courier", 9),
            wrap=tk.WORD,
            relief=tk.SUNKEN
        )
        self.log_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Configure tags for colored output
        self.log_text.tag_config("timestamp", foreground="#6c7086")
        self.log_text.tag_config("info", foreground="#89b4fa")
        self.log_text.tag_config("success", foreground="#a6e3a1")
        self.log_text.tag_config("error", foreground="#f38ba8")
        self.log_text.tag_config("warning", foreground="#f9e2af")
        self.log_text.tag_config("file", foreground="#cba6f7")
    
    def create_status_bar(self):
        """Create status bar"""
        self.status_bar = tk.Label(
            self.root,
            text="✅ Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg=self.colors['accent'],
            fg=self.colors['fg'],
            font=("Arial", 9)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def toggle_password(self):
        """Toggle password visibility"""
        if self.show_password.get():
            self.password_entry.config(show="")
            self.show_password.set(False)
        else:
            self.password_entry.config(show="•")
            self.show_password.set(True)
    
    def clear_password(self):
        """Clear password field"""
        self.password_var.set("")
        self.log("🗑 Password cleared", "INFO")
    
    def select_file(self):
        """Open file dialog to select a file"""
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[
                ("All files", "*.*"),
                ("Encrypted files", "*.enc"),
                ("Encrypted files", "*.encrypted"),
                ("Text files", "*.txt"),
                ("PDF files", "*.pdf")
            ]
        )
        if filename:
            self.selected_file = filename
            self.file_path_var.set(filename)
            self.log(f"📂 Selected: {os.path.basename(filename)}", "FILE")
            self.status_bar.config(text=f"Selected: {os.path.basename(filename)}")
            self.compute_hash_auto()
    
    def compute_hash_auto(self):
        """Auto compute hash when file is selected"""
        if self.selected_file and os.path.exists(self.selected_file):
            try:
                sha256 = hashlib.sha256()
                with open(self.selected_file, 'rb') as f:
                    for chunk in iter(lambda: f.read(8192), b""):
                        sha256.update(chunk)
                hash_value = sha256.hexdigest()
                self.hash_var.set(f"SHA-256: {hash_value[:64]}...")
                self.log(f"🔐 Hash: {hash_value[:32]}...", "HASH")
            except Exception as e:
                self.log(f"⚠️ Hash error: {e}", "ERROR")
    
    def compute_hash_manual(self):
        """Manually compute and verify hash"""
        if not self.selected_file:
            messagebox.showwarning(
                "No File Selected",
                "Please select a file first using the Browse button.",
                parent=self.root
            )
            return
        
        if not os.path.exists(self.selected_file):
            messagebox.showerror(
                "File Not Found",
                f"The file '{self.selected_file}' does not exist.",
                parent=self.root
            )
            return
        
        try:
            self.log("🔍 Computing SHA-256 hash...", "INFO")
            sha256 = hashlib.sha256()
            with open(self.selected_file, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b""):
                    sha256.update(chunk)
            hash_value = sha256.hexdigest()
            
            self.hash_var.set(f"SHA-256: {hash_value}")
            self.log(f"✅ Hash computed: {hash_value[:32]}...", "SUCCESS")
            
            # Standard messagebox with OK button
            messagebox.showinfo(
                "Hash Computed Successfully",
                f"File: {os.path.basename(self.selected_file)}\n\n"
                f"SHA-256 Hash:\n{hash_value}\n\n"
                f"Use this hash to verify file integrity later.",
                parent=self.root
            )
            self.status_bar.config(text="Hash computed")
        except Exception as e:
            self.log(f"❌ Hash failed: {e}", "ERROR")
            messagebox.showerror(
                "Hash Computation Failed",
                f"Error: {str(e)}",
                parent=self.root
            )
    
    def encrypt_file(self):
        """Encrypt the selected file"""
        # Validation
        if not self.selected_file:
            messagebox.showwarning(
                "No File Selected",
                "Please select a file to encrypt using the Browse button.",
                parent=self.root
            )
            return
        
        if not os.path.exists(self.selected_file):
            messagebox.showerror(
                "File Not Found",
                f"The file '{self.selected_file}' no longer exists.",
                parent=self.root
            )
            return
        
        password = self.password_var.get()
        if not password:
            messagebox.showwarning(
                "Password Required",
                "Please enter a password to encrypt the file.\n\n"
                "Password must be at least 4 characters long.",
                parent=self.root
            )
            return
        
        if len(password) < 4:
            messagebox.showwarning(
                "Weak Password",
                "Password is too short! Use at least 4 characters for security.",
                parent=self.root
            )
            return
        
        # Set output path
        original_name = Path(self.selected_file).stem
        output_path = os.path.join(self.output_dir, f"{original_name}_encrypted.enc")
        
        threading.Thread(target=self._encrypt_worker, args=(password, output_path), daemon=True).start()
    
    def _encrypt_worker(self, password, output_path):
        """Worker function for encryption"""
        self.set_buttons_state(False)
        self.progress.start()
        self.log("🔒 Starting encryption...", "INFO")
        self.status_bar.config(text="Encrypting...")
        
        try:
            result = self.encryptor.encrypt_file(self.selected_file, password, output_path)
            self.log(f"✅ Encryption complete!", "SUCCESS")
            self.log(f"📁 Saved: {os.path.basename(result)}", "FILE")
            self.status_bar.config(text=f"Encrypted: {os.path.basename(result)}")
            
            # Standard success dialog with OK button
            messagebox.showinfo(
                "Encryption Successful",
                f"✅ File encrypted successfully!\n\n"
                f"Original: {os.path.basename(self.selected_file)}\n"
                f"Encrypted: {os.path.basename(result)}\n"
                f"Location: {self.output_dir}\n\n"
                f"📁 Hash file saved with .hash extension\n\n"
                f"⚠️ Remember your password - it cannot be recovered!",
                parent=self.root
            )
        except Exception as e:
            error_msg = str(e)
            self.log(f"❌ Encryption failed: {error_msg}", "ERROR")
            self.status_bar.config(text="Encryption failed")
            
            messagebox.showerror(
                "Encryption Failed",
                f"Could not encrypt file.\n\nError: {error_msg}\n\n"
                f"Possible causes:\n"
                f"• File is corrupted\n"
                f"• Disk is full\n"
                f"• Permission denied",
                parent=self.root
            )
        finally:
            self.progress.stop()
            self.set_buttons_state(True)
    
    def decrypt_file(self):
        """Decrypt the selected file"""
        # Validation
        if not self.selected_file:
            messagebox.showwarning(
                "No File Selected",
                "Please select an encrypted file (.enc) to decrypt.",
                parent=self.root
            )
            return
        
        if not os.path.exists(self.selected_file):
            messagebox.showerror(
                "File Not Found",
                f"The file '{self.selected_file}' no longer exists.",
                parent=self.root
            )
            return
        
        password = self.password_var.get()
        if not password:
            messagebox.showwarning(
                "Password Required",
                "Please enter the password used to encrypt this file.",
                parent=self.root
            )
            return
        
        # Set output path
        original_name = Path(self.selected_file).stem
        clean_name = original_name.replace('_encrypted', '').replace('.encrypted', '')
        output_path = os.path.join(self.output_dir, f"{clean_name}_decrypted.txt")
        
        threading.Thread(target=self._decrypt_worker, args=(password, output_path), daemon=True).start()
    
    def _decrypt_worker(self, password, output_path):
        """Worker function for decryption"""
        self.set_buttons_state(False)
        self.progress.start()
        self.log("🔓 Starting decryption...", "INFO")
        self.status_bar.config(text="Decrypting...")
        
        try:
            result = self.encryptor.decrypt_file(self.selected_file, password, output_path)
            self.log(f"✅ Decryption complete!", "SUCCESS")
            self.log(f"📁 Saved: {os.path.basename(result)}", "FILE")
            self.log("✅ Integrity check PASSED", "SUCCESS")
            self.status_bar.config(text=f"Decrypted: {os.path.basename(result)}")
            
            # Standard success dialog with OK button
            messagebox.showinfo(
                "Decryption Successful",
                f"✅ File decrypted successfully!\n\n"
                f"Encrypted: {os.path.basename(self.selected_file)}\n"
                f"Decrypted: {os.path.basename(result)}\n"
                f"Location: {self.output_dir}\n\n"
                f"✓ Integrity verification PASSED\n"
                f"✓ File has not been tampered with\n\n"
                f"Do you want to open the decrypted file?",
                parent=self.root
            )
            
            # Ask if user wants to open the file
            if messagebox.askyesno(
                "Open File",
                f"Decrypted file saved as:\n{os.path.basename(result)}\n\nDo you want to open it now?",
                parent=self.root
            ):
                os.system(f"xdg-open \"{result}\" 2>/dev/null &")
                
        except Exception as e:
            error_msg = str(e)
            self.log(f"❌ Decryption failed: {error_msg}", "ERROR")
            self.status_bar.config(text="Decryption failed")
            
            # Check for common errors
            if "integrity" in error_msg.lower() or "hash" in error_msg.lower():
                messagebox.showerror(
                    "Integrity Check Failed",
                    f"⚠️ FILE INTEGRITY CHECK FAILED!\n\n"
                    f"The file may have been:\n"
                    f"• Tampered with\n"
                    f"• Corrupted\n"
                    f"• Modified after encryption\n\n"
                    f"Error: {error_msg}",
                    parent=self.root
                )
            elif "padding" in error_msg.lower():
                messagebox.showerror(
                    "Decryption Failed",
                    f"Incorrect password or corrupted file.\n\n"
                    f"Possible causes:\n"
                    f"• Wrong password\n"
                    f"• File is not encrypted with this tool\n"
                    f"• File is corrupted\n\n"
                    f"Error: {error_msg}",
                    parent=self.root
                )
            else:
                messagebox.showerror(
                    "Decryption Failed",
                    f"Could not decrypt file.\n\nError: {error_msg}",
                    parent=self.root
                )
        finally:
            self.progress.stop()
            self.set_buttons_state(True)
    
    def clear_all(self):
        """Clear all fields"""
        self.selected_file = None
        self.file_path_var.set("No file selected")
        self.password_var.set("")
        self.hash_var.set("Select a file to compute hash")
        self.log_text.delete(1.0, tk.END)
        self.log("🗑 All fields cleared", "INFO")
        self.status_bar.config(text="Ready - Select a file to begin")
    
    def log(self, message, level="INFO"):
        """Add timestamped and colored message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        self.log_text.insert(tk.END, f"[{timestamp}] ", "timestamp")
        self.log_text.insert(tk.END, f"{message}\n", level.lower())
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def set_buttons_state(self, enabled):
        """Enable/disable buttons during operations"""
        state = tk.NORMAL if enabled else tk.DISABLED
        self.encrypt_btn.config(state=state)
        self.decrypt_btn.config(state=state)

def main():
    root = tk.Tk()
    app = EncryptionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

