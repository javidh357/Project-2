import random
otp = random.randint(1000, 9999)
print("OTP is:", otp)
otp_count = 0

while True:
    try:
        entered_otp = int(input("Enter your 4 Digit OTP: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue
    if otp == entered_otp :
        print("✅✅Verified")
        break
    else:
        print("❌❌Wrong OTP")

        
        otp_count+=1
        if otp_count==3:
            print("You have entered wrong OTP 3 times")
            break
        else:
            print("Enter your OTP again")
