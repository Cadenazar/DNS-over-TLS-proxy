# DNS-over-TLS-proxy
Simple DNS to DNS-over-TLS proxy

This code converts all received DNS UDP packets into DNS-over-TLS packets. This helps to prevent DNS poisoning and sniffing of DNS packets.

To get this script to work, download and run the script as administrator. Next, Change the DNS server used by the device it is installed on to, 127.0.0.1. For windows it will look like below.
![image](https://github.com/Cadenazar/DNS-over-TLS-proxy/assets/88576308/9972e81b-e120-45e0-8d27-df3b3f4884e8)

This will make the computer send all DNS packets to the computer loopback address, ensuring only the computer can read them before they are encrypted. The packets are then encrypted and converted into DNS-over-TLS packets and send to Cloudflares DoT server. The DNS queries are resolved and sent back encrypted to the computer. The DNS queries are decrypted and used by the computer for DNS resolution.
