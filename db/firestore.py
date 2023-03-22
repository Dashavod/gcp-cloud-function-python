import firebase_admin
from firebase_admin import firestore

app = firebase_admin.initialize_app()
def add_document_to_firestore(doc,collection):
    db = firestore.client()
    try:
        db.collection(collection).document().set(doc.__dict__)
    except:
        print( f"Something wrong with add doc {doc} to firestore")
        return "error"
    print(f"Document {doc} added to firestore")
    return id

