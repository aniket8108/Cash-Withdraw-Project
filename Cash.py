print("*** Welcome ***")

print("\nHello I am a Cashier with 10,50,100 Rupees")

print("\nNote : Whatever Amount You Will Enter , You will get Total number of Rupees i.e of 10,50,100")

print("\nFor Example : If Amount is 200 Rps : You will get 2 notes of 100 Rps , 4 notes of 50 Rps and 20 notes of 10 Rps")

n=int(input("\nEnter your amount To be withdrawn -- "))

a=n//10
b=n//50
c=n//100
print("10 Rupees Currency Note Will be ",a)
print("50 Rupees Currency Note Will be ",b)
print("100 Rupees Currency Note Will be ",c)