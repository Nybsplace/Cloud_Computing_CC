import os
import requests
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Get these from your Supabase project
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

BUCKET_NAME = "PDF_buck"
FILE_NAME = "Order.pdf"

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY environment variables are required."
    )

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

# -----------------------------
# Upload file
# -----------------------------
with open(FILE_NAME, "rb") as file:
    response = requests.post(
        f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{FILE_NAME}",
        headers=headers,
        data=file
    )

print("Upload status:", response.status_code)

if response.ok:
    print("File uploaded successfully.")
else:
    print("Upload failed:")
    print(response.text)


# -----------------------------
# Download file
# -----------------------------
response = requests.get(
    f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{FILE_NAME}",
    headers=headers
)

print("\nDownload status:", response.status_code)

if response.ok:
    print("File content:")
    print(response.text)
else:
    print("Download failed:")
    print(response.text)