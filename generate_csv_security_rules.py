####Security Rule enable logs
import sys
import re
import requests
from criandotoken import get_access_token
import json
import getpass
import csv
# import argparse

banner = '''
                                                 
 ####  ######  ####  #    # #####  # ##### #   # 
#      #      #    # #    # #    # #   #    # #  
 ####  #####  #      #    # #    # #   #     #   
     # #      #      #    # #####  #   #     #   
#    # #      #    # #    # #   #  #   #     #   
 ####  ######  ####   ####  #    # #   #     #   
                                                 
                                                           
#####  #    # #      ######  ####      ####   ####  #    # 
#    # #    # #      #      #         #    # #      #    # 
#    # #    # #      #####   ####     #       ####  #    # 
#####  #    # #      #           #    #           # #    # 
#   #  #    # #      #      #    #    #    # #    #  #  #  
#    #  ####  ###### ######  ####      ####   ####    ##   
                                                           
                                                                                      
'''
print("\n")
print(banner)
print("\n")


# # ####VARIABLES
position = "pre" #input("Digite a posicao do: ")
folder = input("Type your folder: ")
limit="200" ##default limit 

client_id = input("Type your client_id: ")
# client_secret = input("Digite o client_secret: ")
client_secret = getpass.getpass("Type your client_secret: ")
tsg_id = input("Type your tsg_id: ")

# ###GERAR TOKEN

access_token = get_access_token(client_id, client_secret, tsg_id)

if access_token:
    print("\n")
    print("Access token obtained successfully!")
    # print(f"Token: {access_token}")
else:
    print("\n")
    print("Failed to get access token.")

# return access_token
# ####LISTAR REGRAS
def list_security_rules():


    try:
        url = "https://api.sase.paloaltonetworks.com/sse/config/v1/security-rules?limit={}&position={}&folder={}".format(limit, position, folder)
    # url = "https://api.sase.paloaltonetworks.com/sse/config/v1/security-rules?position=pre&folder=Remote Networks"

        payload={}
        headers = {
          'Accept': 'application/json',
          'Authorization': f'Bearer {access_token}'
        }

        listobject = requests.request("GET", url, headers=headers, data=payload)
        list_object = listobject.text

        list_object_json = json.loads(list_object)

        listobject.raise_for_status()
        # print()

        # print(type(list_object_json))
        # print(list_object_json)
        return list_object_json
    except requests.exceptions.RequestException as e:
        print("Error Request:", e)
        print("\n")


    # for valor in list_object:                                                                                            
    #     print(valor)  


                # mudando = str(data2)
                # # alterado = mudando.replace("[", "")
                # # alterado = alterado.replace("]","")
                
                # remover=r"\[|\]"
                # validado = re.sub(remover, "", mudando)


def generate_csv(list_object_json):
    # Transforma a resposta JSON em um dicionário Python
    # data = json.loads(json_response)
    data = list_object_json 
    # Abre o arquivo CSV para escrita
    #head id,name,tag,source_zone,source_address,source_user,source_hip,dest_zone,dest_address,dest_user,dest_hip,application,URL Category, Service, Action, Profile Groups, Options
    # id,name,tag,source_zone,source_address,source_user,source_hip,dest_zone,dest_address,dest_user,dest_hip,application,URL Category, Service, Action, Profile Groups, Options
    # print(data['data'][0])
    # print(data['data'][0]['name'])
    #         ID=item['id']
    #         name=item['name']
    #         folder=item['folder']
    #         posi=item['position']    
    #         Action=item['action']
    #         source_zone=item['from']
    #         dest_zone=item['to']
    #         source_address=item['source']
    #         source_user=item.get("['data']['source_user']", "") 
    #         source_hip=item.get("['data']['source_hip']", "")
    #         dest_address=item.get("['data']['destination']", "") 
    #         dest_hip=item.get("['data']['destination_hip']", "") 
    #         dest_user=item.get("['data']['destination_user']", "") 
    #         application=item.get("['data']['application']", "") 
    #         Service=item['service']
    #         Profile_Groups=item.get("['data']['profile_setting']", "") 
    #         tag=item['tag']
    #         description=item.get("['data']['description']", "") 

    # # try:
# option3_value = json_data.get("option3", "")    
# execpt


    with open('security_rules.csv', mode='w', newline='') as file:


    #     # Cria o objeto writer para escrever no arquivo CSV
        writer = csv.writer(file, delimiter="|")

        writer.writerow(['id','name','folder','position','action','from','to','source','source_user','source_hip','destination','destination_hip','destination_user','application','service','profile_setting','tag','description'])
    #     # Escreve o cabeçalho do CSV com as chaves do primeiro elemento do dicionário
    #     writer.writerow(data['data'][0].keys())
       
    #    remover=r"\[|\]\'"  # regex para remover o caracter da lista
    #     # Escreve os dados no arquivo CSV
        for item in data['data']:
            ##opcao manualmente
            ID=item['id']
            name=item['name']
            folder=item['folder']
            posi= item.get("position", "")  #item['position']    
            Action=item['action']
            source_zone= ','.join(item['from'])
            # source_zone=str(source_zone)
            # source_zone = re.sub(remover, "", source_zone)
            dest_zone=','.join(item['to'])
            source_address=','.join(item['source'])
            source_user=','.join(item.get("source_user", "")) 
            source_hip=','.join(item.get("source_hip", ""))
            dest_address=','.join(item.get("destination", "")) 
            dest_hip=','.join(item.get("destination_hip", "")) 
            dest_user=','.join(item.get("destination_user", "") )
            application=','.join(item.get("application", "") )
            Service=','.join(item['service'])
            Profile_Groups=item.get("profile_setting", "")
            tag=','.join(item.get("tag", ""))
            description=item.get("description", "") 

            # print(application)

            writer.writerow([ID,name,folder,posi,Action,source_zone,dest_zone,source_address,source_user ,source_hip,dest_address ,dest_hip ,dest_user ,application ,Service,Profile_Groups ,tag,description ])

    # ##OPCAO COM KEYS VALUES
    #     writer.writerow(data['data'][0].keys())

    #     # Escreve os dados no arquivo CSV
    #     for item in data['data']:
    #         writer.writerow(item.values())
    print("security_rules.csv  created! ")



# Chama a segunda função passando o resultado da primeira como argumento
resultado_da_funcao1 = list_security_rules()
generate_csv(resultado_da_funcao1)

