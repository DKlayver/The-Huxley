def doido(num):
    if num=='0':
        return ''
    else:
        return doido(input())+num+'\n'
    
print(doido(input()))