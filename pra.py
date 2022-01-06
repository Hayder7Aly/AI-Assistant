email_content = {'haider':'007harryjutt@gmail.com','ali':'007razajutt@gmail.com'}
query = 'send email to haider'
for name,adress in email_content.items():
    if name in query:
        print("Yes")
    else:
        print("No")