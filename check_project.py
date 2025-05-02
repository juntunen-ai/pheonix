#!/usr/bin/env python
"""
Check the Phoenix project structure and configuration.
"""
import os
import sys
import json
from pathlib import Path

def check_directory(path, expected_files=None):
    """Check if directory exists and contains expected files."""
    if not os.path.isdir(path):
        return False, f"Directory {path} does not exist."
    
    if expected_files:
        missing_files = [f for f in expected_files if not os.path.exists(os.path.join(path, f))]
        if missing_files:
            return False, f"Directory {path} is missing files: {missing_files}"
    
    return True, f"Directory {path} exists and contains all expected files."

def check_file(path):
    """Check if file exists and print its size."""
    if not os.path.isfile(path):
        return False, f"File {path} does not exist."
    
    size = os.path.getsize(path)
    return True, f"File {path} exists (size: {size} bytes)."

def check_key_file(path):
    """Check if key file exists and is valid JSON."""
    if not os.path.isfile(path):
        return False, f"Key file {path} does not exist."
    
    try:
        with open(path, 'r') as f:
            json_data = json.load(f)
        
        # Check for required fields in service account key
        required_fields = ['type', 'project_id', 'private_key_id', 'private_key', 
                         'client_email', 'client_id']
        
        missing_fields = [field for field in required_fields if field not in json_data]
        if missing_fields:
            return False, f"Key file {path} is missing required fields: {missing_fields}"
        
        return True, f"Key file {path} is valid (project: {json_data['project_id']}, client: {json_data['client_email']})"
    except json.JSONDecodeError:
        return False, f"Key file {path} is not valid JSON."
    except Exception as e:
        return False, f"Error checking key file {path}: {str(e)}"

def main():
    """Run all checks and print results."""
    base_dir = Path(__file__).resolve().parent
    
    print(f"Checking Phoenix project at: {base_dir}")
    print("-" * 60)
    
    checks = [
        # Check directories
        check_directory(base_dir / "phoenix"),
        check_directory(base_dir / "phoenix/core"),
        check_directory(base_dir / "phoenix/api"),
        check_directory(base_dir / "phoenix/ui"),
        check_directory(base_dir / "tests"),
        check_directory(base_dir / "phoenix/config"),
        
        # Check init files
        check_file(base_dir / "phoenix/__init__.py"),
        check_file(base_dir / "phoenix/core/__init__.py"),
        check_file(base_dir / "phoenix/api/__init__.py"),
        check_file(base_dir / "phoenix/ui/__init__.py"),
        check_file(base_dir / "tests/__init__.py"),
        
        # Check configuration files
        check_file(base_dir / "phoenix/core/config.py"),
        check_file(base_dir / ".gitignore"),
        check_file(base_dir / "README.md"),
        check_file(base_dir / "pyproject.toml"),
        
        # Check key file
        check_key_file(base_dir / "phoenix/config/phoenix-key.json"),
    ]
    
    all_passed = True
    for passed, message in checks:
        status = "✅" if passed else "❌"
        print(f"{status} {message}")
        if not passed:
            all_passed = False
    
    print("-" * 60)
    if all_passed:
        print("All checks passed! Your Phoenix project is set up correctly. 🎉")
    else:
        print("Some checks failed. Please fix the issues above.")
    
    # Test import to make sure package is installed correctly
    print("\nTesting imports:")
    try:
        from phoenix.core.config import settings
        print(f"✅ Successfully imported settings (environment: {settings.ENVIRONMENT})")
    except ImportError as e:
        print(f"❌ Failed to import settings: {str(e)}")
        print("   Make sure you've installed the package in development mode: pip install -e .")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())