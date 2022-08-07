#código para retornar o mmc entre dois numeros
#mmc entre dois números é definido como MMC(a,b) = (a * b) / MDC(a,b)

def mmc(num1,num2):
      
    a=num1
    b=num2
      
    resto = None
      
    while resto != 0:

        resto = a % b
            
        a = b
            
        b = resto
        
    return (num1 * num2)/a

num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

print (mmc(num1,num2))

    
