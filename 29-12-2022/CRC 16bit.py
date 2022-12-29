

def xor(a,b):
    res=''
    for i in range(1,len(a)):
        if a[i] == b[i]:
            res = res + '1'
        else:
            res = res + '0'
    return res


def get_checksum(divisor,dividend):
    divisor_len = len(divisor)
    temp = dividend[0:divisor_len]

    while( divisor_len < len(dividend)):
        if temp[0]=='1':
            temp = xor(temp,divisor)+dividend[divisor_len]
        else:
            temp = temp[1:divisor_len] + dividend[divisor_len]
        divisor_len+=1

    if temp[0] == '1':
        temp = xor(temp,divisor)
    
    if len(temp) < len(divisor):
        return '0'+temp
    return temp


def main():

    gen_polynomial = '1001000000100001'
    data = input("Enter data : ")
    modified_data = data + "0"*16 
    checksum_at_sender = get_checksum(gen_polynomial,modified_data)

    
    NoErrorDuringSending = True
    if NoErrorDuringSending:
        print("If there is no error during sending")
        encoded_data = data + checksum_at_sender
        print("checksum_at_sender: {}".format(checksum_at_sender))
        print("checksum_at_reciever: {}".format(get_checksum(gen_polynomial,encoded_data)))
    
    
    ErrorDuringSending = True
    if ErrorDuringSending:
        print("If there is error while sending")
        encoded_data = data + checksum_at_sender
    
        #making error in data
        encoded_data = encoded_data.replace("111","100")
        print("checksum_at_sender: {}".format(checksum_at_sender))
        checksum_at_reciever = get_checksum(gen_polynomial,encoded_data)
        print("checksum_at_reciever: {}".format(checksum_at_reciever))

main()