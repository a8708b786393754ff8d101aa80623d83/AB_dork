data = {
  "api_keys": [
    { "AIzaSyBQggYLTLGkNwN1A2IU-ho3Blb7bKI8S4Q": False },
    { "AIzaSyDBWlnLaAzrqyMRp12_s8Mk3PIJIs1ZkGk": True },
    { "AIzaSyC5sEUyK7zyC4sIxOdYLg9tFTxUxuQzk_g": False }
  ],
  "cse_id": [
    { "4a135df94ee0e5dad": False },
    { "3a3d04f12946b5dbf": True },
    { "cfaac28e5afd61c07": False }
  ], 
  "init_creditials": [
    "AIzaSyDBWlnLaAzrqyMRp12_s8Mk3PIJIs1ZkGk",
    "3a3d04f12946b5dbf"
  ]
}

new_dict = {"api_keys": [], 'cse_id': [], "init_creditials": data["init_creditials"]}
#TODO mettre un jour les identifiant
for api_dict, cse_dict in zip(data['api_keys'], data['cse_id']): 
    for (key_api, value_api), (key_cse, value_cse) in zip(api_dict.items(), cse_dict.items()): 
        if key_api == data["init_creditials"][0] and key_cse == data['init_creditials'][1]: 
            new_dict["api_keys"].append({key_api: True})
            new_dict["cse_id"].append({key_cse: True})
        else: 
            new_dict["api_keys"].append({key_api: False})            
            new_dict["cse_id"].append({key_cse: False})
            
print(new_dict)