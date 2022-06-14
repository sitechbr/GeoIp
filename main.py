import os
from datetime import date
import geoip2.database

def geo_city(ip):
    with geoip2.database.Reader('MMDB/GeoLite2-City.mmdb') as reader:
        response = reader.city(ip)
        return response.country.name, response.city.name

def geo_country(ip):
    with geoip2.database.Reader('MMDB/GeoLite2-Country.mmdb') as reader:
        response = reader.country(ip)
        return response.country.name

def geo_asn(ip):
    with geoip2.database.Reader('MMDB/GeoLite2-ASN.mmdb') as reader:
        response = reader.asn(ip)
        return response.autonomous_system_organization, response.network

def file_to_list(file):
    ip_adr=set()
    with open(file,"r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            ip_adr.add(line.strip())
    return ip_adr

def country2ip(list_ip):
    PATH = 'result'
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    f = open(f"./result/ {date.today()}.csv", 'w')
    for ip in list_ip:
        f.writelines(f"{ip};{geo_country(ip)};{geo_city(ip)};{geo_asn(ip)}\n")
    f.close()


def main():
    print(geo_city("91.227.93.203"))
    print(geo_asn("91.227.93.203"))
    print(geo_country("91.227.93.203"))
    ip=file_to_list("IpList/ip.txt")
    country2ip(ip)

if __name__ == '__main__':
    main()


