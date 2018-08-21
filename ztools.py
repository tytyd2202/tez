import time
import os,sys


#####LOGIN#####
def menu():
 

      
           os.system('clear')
           print
           print '''            \033[1;93m ###############
            \033[1;93m # \033[1;91mPERLU AKSES \033[1;93m#
            \033[1;93m ###############'''
           print
   
 

           
menu()            
log = input("\033[1;91mPassword \033[1;37m= ")

if log == 12345:
      print('\033[1;92mSabar...')
      time.sleep(2)
      os.system('clear')
      print('Sedang Menganalisa DATA...')
      time.sleep(5)
      os.system('clear')
      print('\033[1;92mDone.')
      time.sleep(2)
      os.system('clear')
       
       

else :
	print "\033[1;91mPassword Salah..."
	exit()
	
	
	
	######menu######
def karjok():
                print ''' \033[1;91m
   ___
  |__  /
    / /
   / /_
  /__|\033[1;37m|Tools v.1  '''
                print
                print '''\033[1;91m[\033[1;36m+\033[1;91m]==========\033[0;34mZTools\033[1;91m==========\033[1;91m[\033[1;36m+\033[1;91m]
\033[1;92m#Author  : \033[1;97mIndoKarjok
\033[1;92m#Contact : \033[1;97mtnherp2202@gmail.com
\033[1;92m#Wa      : \033[1;97m0895611252563 & 089620134992
\033[1;92m#IG      : \033[1;97m@Rezadkim
\033[1;92m#Channel : \033[1;97mNganunymous
\033[1;91m[\033[1;36m+\033[1;91m]==========================\033[1;91m[\033[1;36m+\033[1;91m] '''
                print"\033[1;91m *Msg : "
                print " \033[1;34mKpalaOtak kau !!!"
                print " Jangan di recode Qimak "
                print" Tinggal pake apa susahnya njeng? :v "
                   
                print
                time.sleep(1)
                print "\033[1;91m1\033[1;37m. \033[1;92mMBF"
                time.sleep(1)
                print "\033[1;91m2\033[1;37m. \033[1;92mBom-Email"
                time.sleep(1)
                print "\033[1;91m3\033[1;37m. \033[1;92mMaling DATA Kawan"
                time.sleep(1)
                print "\033[1;91m4\033[1;37m. \033[1;92mMaling Nomor Wa Ceue"
                time.sleep(1)
                print "\033[1;91m5\033[1;37m. \033[1;92mSpam all Op "
                time.sleep(1)
                print "\033[1;91m6\033[1;37m. \033[1;92mTools apa aja Yg penting kau senang "
                time.sleep(1)
                print "7. \033[1;91mEXIT"
                time.sleep(1)
                print
                
                 #####Command Program#####

      
#Program Utama
karjok()            
karjok = input("\033[1;91mKarjok \033[1;37m=>>")

def mbf():
  os.system('git clone https://github.com/tytyd2202/tez')
  os.system('cd tez')
  os.system('cd karjok')
  os.system('ls')
  os.system('clear')
  os.system('python2 mbf.py')
      
if karjok == 1:
	mbf()

elif karjok == 2:
	baliho()
    
elif karjok == 3:
                trapesium()
elif karjok == 4:
                jajargenjang()
elif karjok == 5:
                bola()
elif karjok == 6:
                exit()
else :
	print "\033[1;91mUdah NgoPi Blom?..."
	time.sleep(2)
	exit()