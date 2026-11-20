import socket

def port_scanner():
    print("=" * 40)
    print("       SIMPLE PORT SCANNER")
    print("=" * 40)

    target = input("Enter target IP or hostname: ")

    try:
        target_ip = socket.gethostbyname(target)
        print(f"\nScanning target: {target_ip}")

        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if not (1 <= start_port <= end_port <= 65535):
            print("Invalid port range!")
            return

        print("\nScanning in progress...\n")

        open_ports = []

        for port in range(start_port, end_port + 1):
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.5)

            result = sock.connect_ex((target_ip, port))

            if result == 0:
                print(f"Port {port}: OPEN")
                open_ports.append(port)

            sock.close()

        print("\n" + "=" * 40)
        print("          SCAN RESULTS")
        print("=" * 40)
        print(f"Target IP: {target_ip}")
        print(f"Open Ports: {len(open_ports)}")

        if open_ports:
            print("Open port list:", open_ports)
        else:
            print("No open ports found.")

        print("\nScan completed!")

    except socket.gaierror:
        print("Invalid hostname or IP address.")

    except ValueError:
        print("Please enter valid port numbers.")

    except KeyboardInterrupt:
        print("\nScanning interrupted by user.")

if __name__ == "__main__":
    port_scanner()