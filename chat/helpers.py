def get_user_id(user_id, reciever_id, sender_id):
    if user_id == reciever_id.id:
        return sender_id
    else:
        return reciever_id