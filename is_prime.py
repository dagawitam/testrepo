def is_prime(num):
    if num > 1:
        i=2
        d=0
        while i <= num:
            if num%i==0:
                d=d+1
            i=i+1
        if d>1:
            print("False")
        else:
            print("True")
    else:
        print("False")



for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")

