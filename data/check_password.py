def check_password(password):
    l, u, p, d = 0, 0, 0, 0
    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
    specialchar = "$@!#?&*?/._-"
    digits = "0123456789"
    if len(password) >= 8:
        for i in password:
            if i in smallalphabets:
                l += 1
            if i in capitalalphabets:
                u += 1
            if i in digits:
                d += 1
            if i in specialchar:
                p += 1
    if all([l >= 1, u >= 1, p >= 1, d >= 1, l + p + u + d == len(password)]):
        return True, 'True'
    elif l < 1:
        return False, 'Пароль должен содержать прописные буквы'
    elif u < 1:
        return False, 'Пароль должен содержать хотя бы 1 заглавную букву'
    elif p < 1:
        return False, f'В пароле должен хотя бы 1 из специальных символов {specialchar}'
    elif d < 1:
        return False, 'Пароль должен содержать хотя бы 1 цифру'
    elif len(password) < 8:
        return False, 'Пароль должен содержать минимум 8 символов'
    else:
        return False, f'Пароль должен состоять из букв латинского алфавита, цифр и специальных символов ({specialchar})'
