import random

def password(len):
    letters='wertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    numbers='1234567890'
    symbols='!@#$%^&*()'
    all=letters+numbers+symbols
    pas=''.join(random.sample(all,len))
    return pas

if __name__=="__main__":
    print("...password genarator...")
    len=int(input("enter a lenght of password:"))
    print("the password :",password(len))
    


    
