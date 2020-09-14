print "HEY GUYS,MATHS BUDDY IS HERE TO HELP YOU.\nCHOOSE THE SERIES OF SPECIAL NUMBERS YOU WANT TO PRINT OR ENTER A NUMBER TO CHECK WHETHER THE NUMBER IS IN THAT SERIES.\nHERE WE GO..."
while True:
        print "\n\nMENU\n1.ABUNDANT NUMBERS\n2.ARMSTRONG NUMBERS\n3.COMPOSITE NUMBERS\n4.DEFICIENT NUMBERS\n5.EVEN NUMBERS\n6.FIBONACCI NUMBERS\n7.HARSHAD/NIVEN NUMBERS\n8.ODD NUMBERS\n9.PERFECT NUMBERS\n10.PERFECT SQUARES\n11.PRIME NUMBERS\n12.WIEFERICH PRIME NUMBERS\n13.KNOW MORE FROM WEB\n14.EXIT"
        c=input("ENTER YOUR CHOICE: ")
        if c==1:
                print "ABUNDANT NUMBER:In number theory, an abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.\nThe integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16. The amount by which the sum exceeds the number is the abundance.The number 12 has an abundance of 4."
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=>")
                if ch==2:
                        n=input("Enter the number: ")
                        i=1
                        s=0
                        while i<=n:
                                if n%i==0:
                                        s=s+i
                                i=i+1
                        if s>(2*n):
                            print "THE NUMBER IS AN ABUNDANT NUMBER"
                        else:
                            print "THE NUMBER IS NOT AN ABUNDANT NUMBER "
                elif ch==1:
                        n=input("ENTER THE NUMBER LIMIT: ")
                        i=1
                        while i<=n:
                            j=1
                            s=0
                            while j<=i:
                                if i%j==0:
                                    s=s+j
                                j=j+1
                            if s>(2*i):
                                print i
                            i=i+1
                        print "\nNO MORE NUMBERS\nTHE END"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass

        elif c==2:
                print "ARMSTRONG NUMBER:An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits.\nFor example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371. "
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT =>")
                if ch==1:
                        n=input("ENTER THE LIMIT: ")
                        i=100
                        while i<=n:
                                i1=i
                                j=0
                                while i1>0:
                                        j=j+1
                                        i1=i1/10
                                sum=0
                                x=i
                                while(x>0):
                                        d=x%10
                                        sum=sum+pow(d,j)
                                        x=x/10
                                if sum==i:
                                        print i
                                i=i+1
                        print "\nNO MORE NUMBERS\nTHE END"
                        
                elif ch==2:
                        n=input("ENTER THE NUMBER: ")
                        x=n
                        y=n
                        sum=0
                        j=0
                        while x>0:
                                j=j+1
                                x=x/10
                        while y>0:
                                d=y%10
                                sum=sum+(d**j)
                                y=y/10
                        if n==sum:
                                print "THE NUMBER IS AN ARMSTRONG NUMBER"
                        else:
                                print "THE NUMBER IS NOT AN ARMSTRONG NUMBER"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
                        
        elif c==3:
                print "COMPOSITE NUMBER:A COMPOSITE NUMBER is a positive integer that can be formed by multiplying together two smaller positive integers. Equivalently, it is a positive integer that has at least one divisor other than 1 and itself"
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=>")
                if ch==1:
                        n=input("ENTER THE LIMIT: ")
                        j=2
                        while j<=n:
                            f=0
                            i=2
                            while i<=((j/2)):
                                if j%i==0:
                                    f=1
                                    break
                                i=i+1
                            if f==1:
                                print j
                            j=j+1
                        print "\nNO MORE NUMBERS\nTHE END"
                elif ch==2:
                        n=input("ENTER THE NUMBER: ")
                        f=0
                        i=2
                        while i<=n/2:
                            if n%i==0:
                                f=1
                                break
                            i=i+1
                        if f==1:
                            print "THE NUMBER IS A COMPOSITE NUMBER"
                        else:
                            print "THE NUMBER IS NOT A COMPOSITE NUMBER"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==4:
                print "DEFICIENT NUMBER:A deficient number or defective number is a number n for which the sum of divisors σ(n)<2n, or, equivalently, the sum of proper divisors (or aliquot sum) s(n)<n. The value 2n − σ(n) (or n − s(n)) is called the numbers deficiency.\nAs an example, consider the number 21. Its divisors are 1, 3, 7 and 21, and their sum is 32.\n Because 32 is less than 2 × 21, the number 21 is deficient.\nIts deficiency is 2 × 21 − 32 = 10."
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=> ")
                if ch==2:
                        n=input("Enter the number: ")
                        i=1
                        s=0
                        while i<=n:
                                if n%i==0:
                                        s=s+i
                                i=i+1
                        if s<(2*n):
                            print "THE NUMBER IS DEFICIENT/DEFECTIVE NUMBER"
                        else:
                            print "THE NUMBER IS NOT DEFICIENT/DEFECTIVE "
                elif ch==1:
                        n=input("ENTER THE NUMBER LIMIT: ")
                        i=1
                        while i<=n:
                            j=1
                            s=0
                            while j<=i:
                                if i%j==0:
                                    s=s+j
                                j=j+1
                            if s<(2*i):
                                print i
                            i=i+1
                        print "\nNO MORE NUMBERS\nTHE END"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==5:
                print "EVEN NUMBERS:Any integer (not a fraction) that can be divided exactly by 2 is called an Even number.The last digit is 0, 2, 4, 6 or 8.Example:4,6 and 38 are all even numbers"
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=> ")
                if ch==1:
                        n=input("ENTER THE LIMIT ")
                        i=2
                        while i<=n:
                                if i%2==0:
                                        print i
                                i=i+2
                elif ch==2:
                        n=input("ENTER THE NUMBER TO CHECK WHETHER IT IS EVEN")
                        if n%2==0:
                            print "THE NUMBER IS EVEN"
                        else:
                            print "THE NUMBER IS NOT EVEN"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==6:
                print "FIBONACCI NUMBERS:In mathematics, the FIBONACCI NUMBERS are the numbers characterized by the fact that every number after the first two is the sum of the two preceding ones"
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=> ")
                if ch==1:
                	n=input("Enter the number of terms ")
			first=0
			second=1
			print first
			print second
			count=2
			while(count<n):
				next=first+second
				print next
				count=count+1
				first=second
				second=next
		elif ch==2:
                        n=input("ENTER THE NUMBER: ")
                        f=0
			if n==0 or n==1:
				f=1
				print "THE NUMBER IS IN FIBONACCI SERIES"
			first=0
			second=1
			count=2
			while(count<n):
				next=first+second
				if n==count:
					print "THE NUMBER IS IN FIBONACCI SERIES"
					break
				count=count+1
				first=second
				second=next
			if f==0:
				print "THE NUMBER IS NOT IN FIBONACCI SERIES"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==7:
                print "HARSHAD/NIVEN NUMBER: A number that is divisible by the sum of its own digits.\nFor example, 1729 is a Harshad number because 1 + 7 + 2 + 9 = 19 and 1729 = 19x91."
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=> ")
                if ch==1:
                        n=input("ENTER THE LIMIT: ")
                        j=1
                        while j<=n:
                            x=j
                            s=0
                            i=j
                            while i>0:
                                d=i%10
                                s=s+d
                                i=i/10
                            if x%s==0:
                                print x
                            j=j+1
                        print "\nNO MORE NUMBERS\nTHE END"
                elif ch==2:
                        n=input("ENTER THE NUMBER: ")
                        x=n
                        s=0
                        while n>0:
                            d=n%10
                            s=s+d
                            n=n/10
                        if x%s==0:
                                print "THE NUMBER IS HARSHAD/NIVEN NUMBER"
                        else:
                                print "THE NUMBER IS NOT A HARSHAD/NIVEN NUMBER"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==8:
                print "ODD NUMBER:An ODD NUMBER is an integer which is not a multiple of two. If it is divided by two the result is a fraction. One is the first odd positive number."
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=> ")
                if ch==2:
                        n=input("ENTER THE NUMBER TO CHECK WHETHER IT IS ODD: ")
                        if n%2==0:
                            print "THE NUMBER IS NOT ODD"
                        else:
                            print "THE NUMBER IS ODD"
                elif ch==1:
                        n=input("ENTER THE LIMIT: ")
                        i=1
                        while i<=n:
                                if i%2!=0:
                                        print i
                                i=i+2
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==9:
                print "PERFECT NUMBER:In number theory, a PERFECT NUMBER is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum)."
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=>")
                if ch==1:
                        n=input("ENTER THE LIMIT: ")
                        i=1
                        l=0
                        while i<=n:
                                s=0
                                j=1
                                while j<i:
                                        if i%j==0:
                                                s=s+j
                                        j=j+1
                                if s==i:
                                        print i
                                i=i+1
                        print "NO MORE NUMBERS\nTHE END"
                elif ch==2:
                        n=input("ENTER THE NUMBER: ")
                        i=1
                        s=0
                        while i<n:
                                if n%i==0:
                                        s=s+i
                                i=i+1
                        if s==n:
                                print "THE NUMBER ",n," IS A PERFECT NUMBER"
                        else:
                                print n,"IS NOT A PERFECT NUMBER"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==10:
                print "PERFECT SQUARE:In mathematics, a SQUARE NUMBER or PERFECT SQUARE is an integer that is the square of an integer\nIn other words, it is the product of some integer with itself.\nFor example, 9 is a square number, since it can be written as 3x3."
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=> ")
                if ch==1:
                        n=input("ENTER THE NUMBER OF TERMS: ")
                        i=1
                        while i<=n:
                                print i*i
                                i=i+1
                elif ch==2:
                        n=input("ENTER THE NUMBER TO CHECK WHETHER IT IS PERFECT SQUARE OR NOT: ")
                        import math
                        x=int(math.sqrt(n))
                        if (x*x)==n:
                                print "THE NUMBER IS A PERFECT SQUARE"
                        else:
                                print "THE NUMBER IS NOT A PERFECT SQUARE"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==11:
                print "A PRIME NUMBER is a natural number greater than 1 that has no positive divisors other than 1 and itself."
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=> ")
                if ch==1:
                        n=input("ENTER THE LIMIT: ")
                        j=2
                        while j<=n:
                            f=0
                            i=2
                            while i<=j/2:
                                if j%i==0:
                                    f=1
                                    break
                                i=i+1
                            if f==0:
                                print j
                            j=j+1
                elif ch==2:
                	f=0
                        n=input("ENTER THE NUMBER: ")
                        i=2
                        while i<=n/2:
                            if n%i==0:
                                f=1
                                break
                            i=i+1
                        if f==0:
                            print "THE NUMBER IS A PRIME NUMBER"
                        else:
                            print "THE NUMBER IS NOT A PRIME NUMBER"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
                
        elif c==12:
                print "WIEFERICH PRIME: It is a prime number p such that p^2 divides (2^(p-1))-1.\nTherefore connecting these primes with Fermat's little theorem, which states that every odd prime p divides (2^(p-1))-1.\nThe only known Wieferich primes are 1093 and 3511 "
                ch=input("\nENTER\n1.PRINT THE NUMBERS\n2.CHECK WHETHER A NUMBER IS IN IT=> ")
                if ch==1:
                        n=input("ENTER THE LIMIT: ")
                        j=2
                        while j<=n:
                            f=0
                            i=2
                            while i<=j/2:
                                if j%i==0:
                                    f=1
                                    break
                                i=i+1
                            if f==0:
                                p=j
                                x=p*p
                                y=(2**(p-1))-1
                                if y%x==0:
                                    print j 
                            j=j+1
                        print "\nNO MORE NUMBERS\nTHE END"
                elif ch==2:
                        n=input("ENTER THE NUMBER: ")
                        j=n
                        i=2
                        f=0
                        while i<=n/2:
                            if n%i==0:
                                f=1
                                break
                            i=i+1
                        if f==0:
                            p=j
                            x=p*p
                            y=(2**(p-1))-1
                            if y%x==0:
                                print "THE NUMBER IS A WIEFERICH NUMBER"
                            else:
                            	print "THE NUMBER IS NOT A WIEFERICH NUMBER"
                        else:
                                print "THE NUMBER IS NOT A WIEFERICH NUMBER"
                else:
                        print "\nINVALID CHOICE\nTRY AGAIN"
                        pass
        elif c==13:
                import webbrowser
                webbrowser.open('https://sites.google.com/site/mathematicsmiscellany/very-special-numbers')
        elif c==14:
                print "\n\nTHANK YOU FOR USING MY PROGRAM\nMATHS BUDDY \nBY\nDRISHYA K JANARDHANAN"
                break
        else:
                print "\nINVALID CHOICE \nTRY AGAIN"
        
	
	
	 
	
