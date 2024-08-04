def computepay(h, r):
    
    # step 1: split hours into normal and extra
    normal_pay= h if h <= 40 else 40  
    extra_pay= h - 40 if h > 40  else 0

    # step 2: compute the pay
    total= normal_pay * r + extra_pay * r * 1.5
    return total 

hrs = input("Enter Hours:")
rate= input("Enter Rate:")
p = computepay (float(hrs), float(rate))
print("Pay", p)

