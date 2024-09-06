import config
import smtplib
import csv
import time

with open('list.csv', 'r', newline='', encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	# smtpObj = smtplib.SMTP_SSL(config.m_host, config.m_port)
	# smtpObj.login(config.m_login, config.m_pass)
	for row in reader:
		print(row)
		text = str('From: admin@company.ru\nTo: ') + str(row[0]) + str('\nSubject: Тема письма\nContent-type: text/plain; charset="UTF-8";\n\n') + str('Здравствуйте, ') + str(row[1]) + str('\nВ данном письме вы получаете данные для входа в *имя сервиса*\n\nЛогин: ') + str(row[2]) + str('\nПароль: ') + str(row[3]) + str('\n\n\nИнструкция и установочные файлы вы можете найти по ссылке\nhttp://smb.company/instr/\n\nВ случае возникновения вопросов, отправьте их, в ответ на данное сообщение.\nВсего доброго!')
		text = text.encode('utf-8')
		# text = text.decode('utf-8', 'ignore')
		smtpObj.sendmail('admin@company.ru', row[0], text)
		# print(text)
		time.sleep(1)
	# smtpObj.quit()