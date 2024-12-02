def AddHuaWeiVpnInstance():
  with open("Address.txt","r") as file:
    for line in file:
       line=line.replace("\n","")
       D20_vlan = line.split(",")[0]
       D20_address = line.split(",")[1]
       D20_ipv6Address =  line.split(",")[2]
       next_interface = line.split(",")[3]
       next_hop = line.split(",")[4]
       ipv6_next_hop = line.split(",")[5]
       des = line.split(",")[6]
       # 1 新建vpn实例
       add_vpn_instance = """
       #
       ip vpn-instance {0}
        ipv4-family
        ipv6-family
       #""".format(D20_vlan)
       # 后将调度的一个出口vlan划分到某一个vpn实例里面
       add_to_d20_vlan_address = """
       #
       vlan {0}
        description {0}
       #
       #
       interface Vlanif{0}
        description {0}
        ip binding vpn-instance {0}
        ipv6 enable
        ip address {1}
        ipv6 address {2}
       #""".format(D20_vlan, D20_address, D20_ipv6Address)
       # 将此vpn实例（llddce1）缺省下一跳指向出接口网关 如出口有vpn实例则跟出口vpn实例。
       router_nex_hop = """
       #
       ip route-static vpn-instance {0} 0.0.0.0 0.0.0.0 {1} {2} description {4}
       ipv6 route-static vpn-instance {0} :: 0 {1} {3} description {4}
       #""".format(D20_vlan, next_interface, next_hop, ipv6_next_hop,des)
       print("-----------------------------------------------------------------------")
       print(add_vpn_instance,add_to_d20_vlan_address,router_nex_hop)
    file.close()
if __name__ == '__main__':
    AddHuaWeiVpnInstance()
