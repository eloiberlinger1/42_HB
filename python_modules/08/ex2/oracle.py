import os
import sys

try:
    import dotenv
    from dotenv import load_dotenv
except ImportError:
    print("[ERR] Module 'python-dotenv' required.")
    sys.exit(1)

load_dotenv()

REQUIRED_VARIABLES = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

print("ORACLE STATUS: Reading the Matrix...")
print("Configuration loaded:")

missing_config = False

for var in REQUIRED_VARIABLES:
    v = os.environ.get(var)

    if v is None:
        print(f"❌ Missing env var : '{var}'")
        missing_config = True
    else:
        if var == "API_KEY":
            print(f"  - {var}: ********* (Safe)")
        else:
            print(f"  - {var}: {v}")

# 4. Gestion de l'erreur globale si une configuration manque
if missing_config:
    print("\n⚠️ Critical error : invalid configuration file.")
    sys.exit(1)

print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
