def validate(mail):
    """
    simple function to validate email addresses. 
    Rules:
    - must contain exactly one “@” sign
    - the recipient name (the part before the “@” sign) must be between 3 and 24 characters long
    - the recipient name can only contain letters (a-z, A-Z), digits (0-9), dots (.), hyphens (-), and underscores (_)
    - the recipient name cannot start or end with a dot (.), hyphen (-), or underscore (_)
    - the domain name (the part after the “@” sign and before the top-level domain) must be between 3 and 12 characters long
    - the domain name can only contain letters (a-z, A-Z), digits (0-9), dots (.), and hyphens (-)
    - the top-level domain must be one of the following: com, net, org, tech, de, io, edu, gov, co, us, uk, info, biz, me, online   
    
    Challenge by coddy.tech; solved by Rene M. (Jan 2026)
    """
    count = mail.count('@')
    char_recipient = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-'
    char_domain = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    special_char = '.-_'
    recipient = mail.split('@') #list 0 -> email name; 1 -> provider
    domain_parts = recipient[1].split('.')
    tld = ['com','net','org','tech',"de","io","edu","gov","co","us","uk","info","biz","me","online"]
    
    if count != 1: #Check @ sign and amount
        return "Email is invalid"
    
    # Check recipient (recipient@)
    if len(recipient[0]) < 3 or len(recipient[0]) > 24:
        return "Email is invalid"
    
    for sc in special_char:
        if recipient[0][0] == sc or recipient[0][-1] == sc:
            return "Email is invalid"
    
    for c in recipient[0]:
        if c not in char_recipient:
            return "Email is invalid"
    
    # Check Domain (@domain)
    if len(domain_parts[0]) < 3 or len(domain_parts[0]) > 12:
        return "Email is invalid"
    
    for c in domain_parts[0]:
        if c not in char_domain:
            return "Email is invalid"
    
    # Check tld
    if domain_parts[1] in tld:
        return "Email is valid"
    else:
        return "Email is invalid"
    
    return "Email is valid"

if __name__ == "__main__":
    mail = str(input("Enter email:\n"))
    print(validate(mail))