def valid_email(email):
    return "@" in email and email.endswith(".com")


def valid_status(status):
    return status in ("Lead","Customer","Client")
