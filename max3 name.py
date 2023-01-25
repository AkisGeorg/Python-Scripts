onoma1=raw_input('Δώσε  ονομα 1-->')
a=input('Δώσε  επιδοση 1-->')
max=a
winner=onoma1


onoma2=raw_input('Δώσε  ονομα 2-->')
b=input('Δώσε  επιδοση 2-->')
if b>max :
    max=b
    winner=onoma2

onoma3=raw_input('Δώσε  ονομα 3-->')
c=input('Δώσε  επιδοση 3-->')  
if c>max :
    max=c
    winner=onoma3
    

print 'o νικητης ειναι ο ', winner , ' με επιδοση ', max    
