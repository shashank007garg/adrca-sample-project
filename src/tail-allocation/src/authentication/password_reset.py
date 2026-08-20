Content:
# Authentication — Password Reset Service

def generate_reset_link(user_id):
    token = create_token(user_id)
    return f"/reset?token={token}"

def validate_reset_link(token):
    # BUG: link not invalidated after first use
    return is_token_valid(token)

def create_token(user_id):
    return f"token_{user_id}"

def is_token_valid(token):
    return token is not None
