def fun(s):
    try:

        # return True if s is a valid email, else return False

        username, rest = s.split('@')
        company, ext = rest.split(".")
    except ValueError:
        return False
    user = ''.join(i for i in username if i not in "_-")
    return user.isalnum() and company.isalnum() and (0 < len(ext) <= 3)


def filter_mail(emails):
    return list(filter(fun, emails))


n = 3
emails = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)