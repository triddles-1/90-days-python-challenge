import socket

def scan_port(host, port):
    """
    Scan a specific port on the target host.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second

        # Attempt to connect to the port
        result = sock.connect_ex((host, port))

        # Check if the port is open
        if result == 0:
            print(f"Port {port} is open on {host}")
        else:
            print(f"Port {port} is closed on {host}")

        # Close the socket
        sock.close()
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")

def scan_ports(host, ports):
    """
    Scan multiple ports on the target host.
    """
    print(f"Scanning {host}...")
    for port in ports:
        scan_port(host, port)

if __name__ == "__main__":
    # Input the target host and ports to scan
    target_host = input("Enter the target host (e.g., 192.168.1.1 or example.com): ")
    target_ports = input("Enter the ports to scan (e.g., 80,443,8080): ").split(",")

    # Convert port strings to integers
    target_ports = [int(port.strip()) for port in target_ports]

    # Start scanning
    scan_ports(target_host, target_ports)