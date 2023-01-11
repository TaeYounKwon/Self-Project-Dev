import smtplib # STMP사용을 위한 모듈
from email.mime.text import MIMEText # 메일을 보낼 때 메세지의 제목과 본문 설정 

# 세션 생성 (지메일 사용을 위한 STMP 변수, 포트번호(G-MAIL의 경우 587))
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작 (G-MAIL은 보안상의 이유로 SMTP연결을 TLS 모드로 설정해야함)
s.starttls()

# 로그인 인증
s.login('kweont0211@gmail.com', '###')

# 보낼 메시지 설정
msg = MIMEText('내용 : 본문내용 테스트입니다.')
msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'

# 메일 보내기
s.sendmail("kweont0211@gmail.com", "tempest0211@gmail.com", msg.as_string())

# 세션 종료
s.quit()