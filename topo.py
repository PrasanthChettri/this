from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink

class CustomTopology(Topo):
    def __init__(self, num_hosts, num_switches, hosts_per_switch, bandwidth, delay):
        # Initialize topology
        Topo.__init__(self)

        # Create switches
        switches = []
        for i in range(num_switches):
            switch = self.addSwitch(f's{i + 1}', cls=OVSSwitch)
            switches.append(switch)

        # Create hosts and connect them to switches
        hosts = []
        for i in range(num_hosts):
            host = self.addHost(f'h{i + 1}')
            hosts.append(host)

            switch_index = i // hosts_per_switch
            switch = switches[switch_index]
            self.addLink(host, switch, bw=bandwidth, delay=delay)

    def set_controller(self, controller_ip, controller_port):
        controller = RemoteController('controller', ip=controller_ip, port=controller_port)
        self.addController(controller)

def run_topology(S, heads):
    # Topology parameters
    NUM_HOSTS = len(S)
    NUM_SWITCHES = len(heads)
    HOSTS_PER_SWITCH = math.ceil(NUM_HOSTS / NUM_SWITCHES)
    BANDWIDTH = 10  # Link bandwidth in Mbps
    DELAY = '5ms'  # Link delay

    # Create topology
    topo = CustomTopology(NUM_HOSTS, NUM_SWITCHES, HOSTS_PER_SWITCH, BANDWIDTH, DELAY)

    # Set the Ryu controller's IP address and port
    CONTROLLER_IP = '127.0.0.1'  # Replace with the actual IP address of the Ryu controller
    CONTROLLER_PORT = 6633  # Replace with the actual port number of the Ryu controller

    topo.set_controller(CONTROLLER_IP, CONTROLLER_PORT)

    # Add cluster head nodes to the topology
    for i, head in enumerate(heads):
        switch_name = f's{i + 1}'
        host_name = f'h{i + 1}'
        switch = topo.getNodeByName(switch_name)
        host = topo.getNodeByName(host_name)
        topo.addLink(host, switch, bw=BANDWIDTH, delay=DELAY)

    # Add member nodes to the corresponding cluster head switches
    for head in heads:
        switch_name = topo.getClusterSwitch(head)
        switch = topo.getNodeByName(switch_name)
        for member in head.members:
            member_name = topo.getHostByIndex(member.id)
            member_host = topo.getNodeByName(member_name)
            topo.addLink(member_host, switch, bw=BANDWIDTH, delay=DELAY)

    # Create Mininet network
    net = Mininet(topo=topo, link=TCLink)

    # Start the network
    net.start()

    # Perform any additional network configuration or testing

    # Stop the network
    net.stop()


if __name__ == '__main__':
    run_topology()

