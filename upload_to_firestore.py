import json
import firebase_admin
from firebase_admin import credentials, firestore

# Step 1: Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Step 2: Load attendance data
with open("fake_attendance_data.json", "r") as f:
    data = json.load(f)

# Step 3: Upload to Firestore
for usn, record in data.items():
    try:
        db.collection("attendance").document(usn).set(record)
        print(f"✅ Uploaded data for {usn}")
    except Exception as e:
        print(f"❌ Error uploading {usn}: {e}")

print("🎉 Bulk upload completed.")
