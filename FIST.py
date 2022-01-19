import json

def is_valid(smc_type): #checks if smc_type is valid
    if smc_type == 'vmt':
        return True
    elif smc_type == 'flt':
        return True
    elif smc_type == 'nfl':
        return True
    else:
        return False

def parse_vmt(contract):
    try: 
        contract.get('value')
        contract.get('seller')
        contract.get('product')
    except:
        return False
    return True

def parse_flt(contract):
    try: 
        contract.get('value')
        contract.get('seller')
        contract.get('product')
        contract.get('land-id')
        contract.get('land-id')
    except:
        return False
    return True


def parse_contract(filename):
    try:
        contract = json.load(open(filename)) # Tries to load the contract
    except:
        return False

    if(is_valid(smc_type) is False): #validate if the contract is valid
        return print("Not a valid contract")
    return contract


parse_contract('vmt.json')