from functions.get_int import interfaces_arr, subnet_mask_result, ip_address_result

def convert_mask(subnet_mask_str):
    binary_mask = ''.join(format(int(x), '08b') for x in subnet_mask_str.split('.'))
    cidr = sum(bit == '1' for bit in binary_mask)
    return '/' + str(cidr)

for i in range(len(interfaces_arr)):
    converted_mask = convert_mask(subnet_mask_result.split('\n')[i])
    # Subnet in CIDR format
    subnet_cidr = ip_address_result.split('\n')[i] + converted_mask