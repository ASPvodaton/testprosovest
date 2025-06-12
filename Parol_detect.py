import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
num = 0
ch_up = ''
ch_lo = ''
sim = ''
sim_il1 = ''
ind = 0
paswg = []
def generate_password(length, chars):
    length = leng_pas
    print ('str', chars)
    chars = [i for i in chars]
    random.shuffle(chars)
    print('1', chars)
    for _ in range(length):
        paswg.append(random.choice(chars))
        print(paswg)
    
    print(''.join(paswg))    
    

pass_num = int(input('Write quantity of passwords: '))


while pass_num > 0:
    
    leng_pas = int(input('Length of password: '))
    num = int(input('includ numbers: if YES - input: 1, if NO - input 0: '))
    ch_up = input('Включать ли прописные буквы ABC...- YES: ').lower()
    ch_lo = input('Включать ли строчные буквы abc... - yes: ').lower()
    sim = input('Включать ли символы !#$%&*+-=?@^_?: - Yes: ').lower()
    sim_il1 = input('Исключать ли неоднозначные символы il1Lo0O? input - YES: ').lower()
    if num != 0:
        chars += digits
    if ch_up == 'yes':
        chars += ch_up
    if ch_lo == 'yes':
        chars += ch_lo
    print('while', chars)
    if sim == 'yes':
        for i in 'il1Lo0O':
            ind = chars.find(i)
            chars = chars[ : ind] + chars[ind + 1 : ]
    generate_password(leng_pas, chars)             
    
    pass_num -= 1
    if pass_num != 0:
        chars = ''
        num = 0
        ch_up = ''
        ch_lo = ''
        sim = ''
        sim_il1 = ''
        paswg = []
