from django.shortcuts import render, HttpResponse
from faker import Faker as fk
import time
from email.header import decode_header, make_header
from pprint import pprint
import IPython
from dns import resolver, reversename
import json
import random
from netaddr import IPNetwork
import pydnsbl
from pydnsbl import DNSBLIpChecker, providers
from pydnsbl.providers import BASE_PROVIDERS, Provider



# from dns import NoAnswer, NXDOMAIN, NoNameservers, Timeout
# from dns import resolver #import the module

# Create your views here.
def index(requests):
    return render(requests, 'dashboard.html')
def dnsCreator(requests):
    return render(requests, 'dnsCreator.html')
def RandomWords(requests):
    return render(requests, 'RandomWords.html')
def HeaderDecoder(requests):
    return render(requests, 'HeaderDecoder.html')
def dnsCheck(requests):
    return render(requests, 'dnsCheck.html')
def ReverseCheck(requests):
    return render(requests, 'ReverseCheck.html')
def DnsBl(requests):
    return render(requests, 'DnsBl.html')
def IpClassConverter(requests):
    return render(requests, 'IpClassConverter.html')


def IpClassGenerator(requests):
    if requests.method == 'POST':
        ips_list = str(requests.POST['ip_list']).strip().split()
        response_list =[]
        for ip in IpValidation(ips_list):
            response_list.append(ip+"\n")
    return HttpResponse(response_list, content_type="text/plain")

def DnsBlGenerator(requests):
    providers = [Provider('zen.spamhaus.org'), Provider('b.barracudacentral.org')]
    checker = DNSBLIpChecker(providers=providers)
    if requests.method == 'POST':
        ips_list = str(requests.POST['ip_list']).strip().split()
        client_desire = requests.POST['ip_type']
        response_list = {}
        if ips_list[0].split(".")[0].isnumeric():
            response = checker.bulk_check(IpValidation(ips_list))
        else:
            response = checker.bulk_check(ips_list)

        for result in response:
            response_list[result.addr] = result.detected_by

    final_list = []
    for _ in response_list:
        if client_desire == "all":
            final_list.append(str(_) + ": " + str(response_list[_])+"\n")
        elif (len(response_list[_]) == 0) and (client_desire == "good"):
            final_list.append(str(_) + ": " + str(response_list[_])+"\n")
        elif (len(response_list[_]) != 0) and (client_desire == "bad"):
            final_list.append(str(_) + ": " + str(response_list[_])+"\n")

    return HttpResponse(final_list, content_type="text/plain")




def ReverseGenerator(requests):
    if requests.method == 'POST':
        ips_list = str(requests.POST['ip_list']).strip().split()
        client_desire = requests.POST['ip_type']
        verified_list = []
        for ip in IpValidation(ips_list):
            result =  str(DnsFunction(reversename.from_address(ip), "PTR")[0])
            if (client_desire == "good") and (result != "g"):
                verified_list.append(result+"\n")
            elif (client_desire == "bad") and (result == "g"):
                verified_list.append(ip+"\n")
            elif (client_desire == "all") and (result == "g"):
                verified_list.append(ip+"\n")
            elif (client_desire == "all") and (result != "g"):
                verified_list.append(result+"\n")
        return HttpResponse(verified_list, content_type="text/plain")

def HeaderDecoderGenerator(requests):
    if requests.method == 'POST':
        headers_list = requests.POST['headers_list']
        headers_list = [_+'\n' for _ in headers_list.split("\n") ]
        decoded_list = [make_header(decode_header(_)) for _ in headers_list ]
        # decoded_list = [ _ for _ in decoded_list.values() ]
        pprint(decoded_list)
        # decoded_list = make_header(decode_header(headers_list))
        # decoded_list = str(decoded_list).split("%0A")
        return HttpResponse(decoded_list, content_type="text/plain")

def RandomWordsGenerator(requests):
    if requests.method == 'POST':
        words_nr = requests.POST['words_nr']
        random_words = [_+"\n" for _ in fk().words(int(words_nr))]
        # print(random_words)
        return HttpResponse(random_words, content_type="text/plain")


def dnsGenerator(requests):
    if requests.method == 'POST':
        posted_words = requests.POST['wordslist'].strip().split()
        if len(posted_words) < 2:
            posted_words = open("words.txt", 'r+').read().strip().split()

        dnslenght  = int(requests.POST['dnslenght'].strip())
        dnsnumber  = int(requests.POST['dnsnumber'].strip())
        dnstld  = requests.POST['dnstld'].strip()
        buy_domains = []

        while dnsnumber:
            domain_name = random.choice(posted_words).strip() + random.choice(posted_words).strip()
            if len(domain_name) <= dnslenght:
                domain = domain_name + "." + dnstld
                if DnsFunction(domain) == "good":
                    buy_domains.append(domain+"\n")
                    dnsnumber = dnsnumber-1


        return HttpResponse(buy_domains, content_type="text/plain")

def dnsChecker(requests):
    if requests.method == 'POST':
        domainslist = requests.POST['domainslist'].split()
        checked_domains = {}
        for domain in domainslist:
            checked_domains[domain] = DnsFunction(domain)
        client_desire = requests.POST['domainstype']
        final_list = []
        for result in checked_domains:
            if checked_domains[result] == client_desire:
                final_list.append(result+"\n")

        return HttpResponse(final_list, content_type="text/plain")

#Other functions
def DnsFunction(domain, type = "NS"):
                try:
                    # dnss =  resolver.query(domain, "NS")
                    dnss =  resolver.query(domain, type)
                    if dnss:
                        if type == "PTR":
                            return dnss
                        # print("Cumparat: " + str(domain))
                        return  "bad"
                    else:
                        # print("Good: " + str(domain))
                        return "good"
                except resolver.NoAnswer as e:
                    # print ('NoAnswer good: ' + str(domain))
                    return "good"
                except resolver.NXDOMAIN as e:
                    # print ('NXDOMAIN good: ' + str(domain))
                    return "good"

                except resolver.NoNameservers as e:
                    # print ('NoNameservers bad: ' + str(domain))
                    return  "bad"
                except resolver.Timeout as e:
                    # print ('Timeout bad: ' + str(domain))
                    return  "bad"

                except:
                    print ("Nu o sa creeze acest domeniu")
                    return  "bad"

def IpValidation(ips_list):
    class_list = []
    ip_list = []
    for ips in ips_list:
        if "/" in ips:
            for ip in IPNetwork(ips):
                class_list.append(str(ip))
        else:
            ip_list.append(ips)
    return (class_list + ip_list)
