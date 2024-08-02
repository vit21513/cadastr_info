import json

from rosreestr_api.clients.rosreestr import RosreestrAPIClient, AddressWrapper, PKKRosreestrAPIClient

api_client = RosreestrAPIClient()
temp = PKKRosreestrAPIClient()

# print(temp.get_building_by_cadastral_id("23:35:0550004:12"))
# print(temp.get_parcel_by_cadastral_id("23:35:0550004:3"))


# get objects by address
# macro_regions = api_client.macro_regions
# try:
#     with open("data.json", "w") as json_file:
#         json.dump(macro_regions, json_file, ensure_ascii=False)
# except:
#     print("not loaded")
#
# m_regs_to_regs = api_client.macro_regions_to_regions
# try:
#     with open("region.json", "w") as json_file:
#         json.dump(m_regs_to_regs, json_file, ensure_ascii=False)
# except:
#     print("not loaded")




with open("subject.json", 'r') as fp:
    subject = json.load(fp)
with open("region.json", 'r') as fp:
    raions = json.load(fp)

find_reg_id = [m['id'] for m in subject if m['name'] == 'Краснодарский край'][0]

# find_regions = [m_regs_to_regs[reg_id] for reg_id in m_regs_to_regs if reg_id == find_reg_id][0]
# region_id = [r['id'] for r in find_regions if r['name'] == 'Южный'][0]
# region_id = [r['id'] for r in find_regions if r['name'] == 'Южный'][0]
# address_with_ids = AddressWrapper(
#     macro_region_id=find_reg_id, region_id=region_id,
#     street_name='Красного маяка', house_number=22, house_building=2,
#     apartment=187)
# address_with_names = AddressWrapper(
#     macro_region_name='Москва', region_name='Южный',
#     street_name='Красного маяка', house_number=22, house_building=2,
#     apartment=187)
# api_client.get_objects_by_address(address_with_ids)
# print(api_client.get_objects_by_address(address_with_names))
