def solution(S, C):
    names = S.split('; ')
    email_counts = {}
    company_lower = C.lower()
    res = []
    for name in names:
        parts = names.split()
        first = parts[0].lower()
        last_processed = parts[-1].replace('-', '').lower()[:8]
        locaal_base = f"{first}.{last_processed}"
        base_email = f"{locaal_base}@{company_lower}.com"
        count = email_counts.get(base_email, 0)
        if count == 0:
            f = base_email
        else:
            f = f"{locaal_base}{count + 1}@{company_lower}.com"
        email_counts[base_email] = count + 1
        res.append(f"{name} <{f}>")

    return '; '.join(res)

