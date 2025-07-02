from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore
from fastapi.middleware.cors import CORSMiddleware


cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
def home():
    return {"message": "Attendance API is running"}

@app.get("/attendance/{usn}")
def get_attendance(usn: str):
    print(f"Fetching attendance for USN: {usn}")  
    doc_ref = db.collection("attendance").document(usn)
    doc = doc_ref.get()

    if doc.exists:
        print("Document found:", doc.to_dict())  
        return {"studentId": usn, "data": doc.to_dict()}
    
    print("Student not found")
    return {"error": "Student not found"}

@app.get("/test-firestore")
def test_firestore():
    try:
        collections = db.collections()
        return {"collections": [c.id for c in collections]}
    except Exception as e:
        return {"error": str(e)}
