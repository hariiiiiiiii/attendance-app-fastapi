from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Attendance API is running"}

# Fetch attendance for a student
@app.get("/attendance/{student_id}")
def get_attendance(student_id: str):
    doc_ref = db.collection("attendance").document(student_id)
    doc = doc_ref.get()

    if doc.exists:
        return {"studentId": student_id, "data": doc.to_dict()}
    return {"error": "Student not found"}
