text = '''My name is Mariya I am a 20-year-old student from Donetsk.
I study at the university in my native town and my future profession is bookkeeping. 
I live with my parents and my elder sister Lena. We are a friendly family.'''
line=input("").split()
cnt=0
for i,s in enumerate(line):
    if s.isdigit():
        cnt+= len(s)
    if cnt == 0:
        print("числа не обнаружены")
else:
    print("",cnt)
