from mininet.topo import Topo


class MyTopo(Topo):
    def __init__(self):

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        leftHost1 = self.addHost('h1')
        leftHost2 = self.addHost('h2')
        rightHost1 = self.addHost('h3')
        rightHost2 = self.addHost('h4')
        leftSwitch = self.addSwitch('s1')
        rightSwitch = self.addSwitch('s2')

        # Add links
        self.addLink(leftHost2,leftSwitch)
        self.addLink(leftHost1, leftSwitch)
        self.addLink(leftSwitch, rightSwitch)
        self.addLink(rightSwitch, rightHost1)
        self.addLink(rightSwitch, rightHost2)

topos = {'myfirsttopo': (lambda: MyTopo())}
