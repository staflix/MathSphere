import DNS


def is_valid_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        return False
    domain = parts[1]
    try:
        DNS.DiscoverNameServers()
        response = DNS.Request().req(name=domain, qtype='A')
        if response.answers:
            return True
        else:
            return False
    except DNS.Base.ServerError:
        return False

