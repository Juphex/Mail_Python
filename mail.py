import smtplib
import hashlib
from email.message import EmailMessage

smtp_server = ""
username = ""
password = ""

number_mails = 1

subject_ = ""
from_ = ""
to_ = ""
message_ = ""

add_hash = True

if __name__ == "__main__":
    #hash
    m = hashlib.sha256()

    for i in range(number_mails):    
        msg = EmailMessage()
        msg['Subject'] = subject_
        msg['From'] = from_
        msg['To'] = to_
        msg.set_content(message_)

        if(add_hash):
            temp = str(i)
            m.update(bytes(temp,encoding="utf8"))
            msg.set_content(msg.get_content() + "\n" + m.hexdigest())

        # Send the message
        s = smtplib.SMTP(smtp_server)
        s.login(username, password)
        s.send_message(msg)

    s.quit()
