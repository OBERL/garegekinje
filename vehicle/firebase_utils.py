from .firebase_config import db

def get_current_distance(request_id):
    try:
        ref = db.reference(f'{123}/totalDistance')
        current_distance = ref.get()
        return current_distance
    except Exception as e:
        print(f"Error fetching data from Firebase for request {request_id}: {e}")
        return None

def save_target_distance_to_firebase(vehicle_no, target_distance):
    ref = db.reference(f'vehicles/{vehicle_no}/targetDistance')
    ref.set(target_distance)