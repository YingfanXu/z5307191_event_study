#First clear Spaces and lowercase letters
cur_AAA = fron_cur.upper().strip()
cur_BBB = to_cur.upper().strip()
# Then check for compliance with the ISO standard, that is, each currency code must consist of 3 letters
if len(cur_AAA) != 3:
raise Exception(f'from_cur must be ISO code, not {from_cur}')
if len(cur_BBB) != 3:
raise Exception(f'to_cur must be ISO code, not {to_cur}')
