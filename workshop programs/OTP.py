import math , random
a=int(input('enter your otp length:'))
i=0

def generateOTP():
    digits = "abcdefghijklmnopqrstuvwxyz"
    OTP=""

    for i in range(a):
        OTP +=digits[math.floor(random.random()*10)]
    return OTP

print("your otp is :", generateOTP())

