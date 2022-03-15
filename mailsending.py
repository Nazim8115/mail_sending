import smtplib
import re
mail_id=["examples@gmail.com","nndjdjdjjdjjd","jdjjdhdhhhdh","ysyshhdhddhdgdgdfgdf"]# here you can add email id
mail="type here mail id "
password="type here password"
c=0
for i in mail_id:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, i)):
        if c>=3:
            break
        else:
            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login(mail,password)
            
            subject="this is test mail"
            
            body="hi how are you ! i will be succsessful!"
            
            msg=f'Subject: {subject}\n\n{body}'
            
            server.sendmail(mail,mail_id,msg)
            
            print("mail sent successfull")
            
            server.quit()
    else:
        c+=1
        print("mail id not valid")
        

    
