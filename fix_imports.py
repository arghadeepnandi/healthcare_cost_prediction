import os
import re

def fix_imports_in_file(filepath):
    """Fix imports from logs.src to src"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace logs.src imports with src imports
        new_content = re.sub(r'from logs\.src\.', 'from src.', content)
        new_content = re.sub(r'import logs\.src\.', 'import src.', new_content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Fixed: {filepath}")
            return True
        else:
            print(f"⏭️  Skipped (no changes needed): {filepath}")
            return False
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

def main():
    """Fix all Python files in src directory"""
    print("🔧 Fixing imports in all Python files...")
    print("=" * 50)
    
    fixed_count = 0
    
    # Walk through src directory
    for root, dirs, files in os.walk('src'):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                if fix_imports_in_file(filepath):
                    fixed_count += 1
    
    print("=" * 50)
    print(f"✅ Fixed {fixed_count} file(s)")
    print("\nNow run: python train_model.py")

if __name__ == "__main__":
    main()