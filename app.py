import secrets

def generate_otp(length=8):

    return "" .join(str(secrets.randbelow(10)) for _ in range(length))



print("Generate OTP : ", generate_otp())





def otp_generate(length=6):
    return "".join(str(secrets.token_hex(5)) for _ in range(length))

print("Generate OTP2 : ", otp_generate())




