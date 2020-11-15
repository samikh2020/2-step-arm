import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='filename')
args = parser.parse_args()

with open(args.filename) as food:
    data = json.load(food)

for value in data['vm_private_ips']['value'].values():
   print(value)


access = data['network']['vms']
for attributes in access:
    inside_attribute = attributes['attributes']
    for ipv4 in inside_attribute['access_ip_v4']:
            print(ipv4,end='' )

# print (type(data))
# ['jenkins-agent-vm-1']
# ip_address= key['jenkin.+', key]
# data = ["value"][0]["jenkins?"]
#['vms']['attributes']['access_ip_v4'].values()
#        if 'value'.keys() == 'name'.values():
   # for attribute in access['attributes']['access_ip_v4']:

         #   print(type(attribute))

#for access_ip_v4 in attributes['access_ip_v4'].values():
    #print(access_ip_v4)

#for inside_attribute in attributes:
    #for ipv4 in inside_attribute['access_ip_v4']:
        #print(ipv4)
