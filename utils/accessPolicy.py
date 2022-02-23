

def get_policy_with_id():
    return True


def access_policy(msg, data):
    if msg.sender is not data.Owner:
        pass

    if not data.FileID:
        return False
    else:
        ap = get_policy_with_id(data.FileID)
        return ap


