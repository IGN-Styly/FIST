import json


def is_valid(smc_type):  # checks if smc_type is valid
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
        contract.get('land-id').get('1')
    except:
        return False
    return True


def parse_nfl(contract):
    try:
        contract.get('value')
        contract.get('seller')
        contract.get('product')
        contract.get('land-id')
        contract.get('land-id').get('1')
    except:
        return False
    return True

def parse_type(smc_type, contract):
    if smc_type=='vmt':
        return parse_vmt(contract)
    elif smc_type=='flt':
        return parse_flt(contract)
    elif smc_type == 'nfl':
        return parse_nfl(contract)

def parse_contract(json):
    try:
        contract = json.load(json)  # Tries to load the contract
        smc_type = contract.get('type')
    except:
        return False

    if(is_valid(smc_type) is False):  # validate if the contract type is valid
        return False
    
    if parse_type(smc_type=smc_type, contract=contract) is True:
        return contract
    else:
        return False
