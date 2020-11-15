import json
import argparse
#parser
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='filename')
args = parser.parse_args()
#loading file
with open(args.filename) as food:
    data = json.load(food)

if args.filename == 'input2.json':
 #for keys in data['vm_private_ips']['value'].keys():
    for value in data['vm_private_ips']['value'].values():
     access = data['network']['vms']
     for attributes in access:
         inside_attribute = attributes['attributes']
         for ipv4 in inside_attribute['access_ip_v4']:
             print(ipv4, value),
else:
#printing ip address values
    for value in data['vm_private_ips']['value'].values():
        print(value)

#for keys in data['vm_private_ips']['value'].keys():
   #print(keys)