import os.path
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendmail(from_addr, to_addr, subject, content, files = []):
    # 발송 정보 설정
    content_type ="html"
    username = "cj562270@gmail.com"
    password = "xxquvavwadadxirc"
    smtp = 'smtp.gmail.com'
    port = 587


    # 메일 객체 생성하기

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['Form'] = from_addr
    msg['To'] = to_addr

    # 본문 설정
    msg.attach(MIMEText(content, content_type))


    # 파일 첨부

    if files:
        for f in files:
            with open(f, 'rb') as a_file:
                basename = os.path.basename(f)
                # 파일의 내용과 파일이름을 메일에 첨부할 형식으로 변환
                part = MIMEApplication(a_file.read(), Name = basename)

                # 파일첨부
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename
                msg.attach(part)

    # 메일 발송 처리

    mail = SMTP(smtp)
    mail.ehlo()
    mail.starttls()
    mail.login(username, password)
    mail.sendmail(from_addr, to_addr, msg.as_string())
    mail.quit()