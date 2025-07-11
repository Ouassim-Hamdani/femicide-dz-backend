from bson import ObjectId
def convert_ids(data):
    """
    Convert ObjectId in dictionary or list to string representation.
    """
    if isinstance(data, dict):
        return {k: convert_ids(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_ids(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data