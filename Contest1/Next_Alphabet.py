c = input().strip()
if(c == 'z'):
    next_char = 'a'
else:
    next_char = chr(ord(c) + 1) 
       
print(next_char)