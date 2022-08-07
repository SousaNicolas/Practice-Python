#código para retornar o mmc entre dois numeros
#mmc entre dois números é definido como MMM(a,b) = (a * b) / MDC(a,b)

def mmc(num1,num2)

  num1 = int(input("Digite um número inteiro:"))
  num2 = int(input("Digite outro número inteiro:"))
  
  a=num1
  b=num2
  
  resto = None
  
  while resto is not 0:
    resto = a % b
    
    a = b
    
    b = resto
    
   return (num1 * num2) / a

#Test
assert 60 == mmc(12,20)
    
