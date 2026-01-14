import os

print("Current working directory:", os.getcwd())
print("\nChecking paths:")

paths = [
    'notebook/medical_expenses.csv',
    'notebook\\medical_expenses.csv',
    os.path.join('notebook', 'medical_expenses.csv')
]

for path in paths:
    exists = os.path.exists(path)
    print(f"{path} -> Exists: {exists}")

# List files in notebook folder
print("\nFiles in notebook folder:")
if os.path.exists('notebook'):
    print(os.listdir('notebook'))
else:
    print("notebook folder doesn't exist!")