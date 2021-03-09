n = 5
output=''
print(n)
while n > 1:
    bin_bit = n % 2
    print(bin_bit)
    n = n // 2
    print(n)
    output=str(bin_bit)+output

if n==1:
    output='1'+output

print(output)
