import re
import poplib

p3 = poplib.POP3_SSL(host='server')
p3.user('username')
p3.pass_('pw')
print('Emails:')
for i in range(len(p3.list()[1])):
    for j in p3.retr(i + 1)[1]:
        print(j)
        if j.startswith(b'Subject: '):
            print(j[9:].decode('utf-8'))
            if bool(re.match(j[9:13].decode('utf-8'), 'junk', re.IGNORECASE)):
                p3.dele(i + 1)
p3.quit()
