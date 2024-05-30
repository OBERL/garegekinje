from .firebase_config import db

def get_current_distance(request_id):
    try:
        ref = db.reference(f'{123}/totalDistance')
        current_distance = ref.get()
        return current_distance
    except Exception as e:
        print(f"Error fetching data from Firebase for request {request_id}: {e}")
        return None
