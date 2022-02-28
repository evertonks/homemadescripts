import string
import random

from pyfiglet import Figlet

banner = Figlet(font='ogre')

print('\n'+'\x1b[1;36m'+ banner.renderText('Pwd Generator') +'\x1b[0m')

pwd_length = int(input('\U0001F4AC Password length: '))
chars = string.ascii_letters + string.digits + '@$#,.,#$@'
rnd = random.SystemRandom()

print("\n\n\U0001F511 " + ''.join(rnd.choice(chars) for i in range(pwd_length)))
print('\U00002796' * 40)
