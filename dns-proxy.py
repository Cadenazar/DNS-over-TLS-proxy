import socket
import ssl
from dnslib import DNSRecord

# Define the DNS server to forward requests to
DNS_SERVER = ("1.1.1.1", 853)

def proxy_dns(client_request, client_address):
    # Connect to the DNS server
    context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
    with socket.create_connection(DNS_SERVER,timeout=5) as tls_socket:
        with context.wrap_socket(tls_socket, server_hostname=DNS_SERVER[0]) as dot_socket:
          # Forward the request to the DNS server
          dot_socket.send(build_query(client_request))
          print(DNSRecord.parse(client_request))
          # Receive the DNS response from the server
          server_response = dot_socket.recv(4096)
          # Forward the response to the client
          with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            print(server_response[2:])
            client_socket.sendto(server_response[2:], client_address)

def build_query(packet):
        packet_len = bytes([00]) + bytes([len(packet)])
        packet = packet_len + packet
        return packet

if __name__ == '_main_':
    # Create a socket to accept incoming DNS requests
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
        proxy_socket.bind(('127.0.0.1',53))  # Listen on port 53 for DNS
        print("DNS proxy is listening on port 53...")

        while True:
            client_request, client_address = proxy_socket.recvfrom(512)
            print(f"Received DNS query from {client_address}")
            proxy_dns(client_request, client_address)