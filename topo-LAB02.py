"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
	"Simple topology example."

	def __init__( self ):
		"Create custom topo."

		# Initialize topology
		Topo.__init__( self )

		# Add hosts and switches
		sHost1 = self.addHost( 'h1' )
		sHost2 = self.addHost( 'h2' )
		sHost3 = self.addHost( 'h3' )
		sHost4 = self.addHost( 'h4' )
		cSwitch = self.addSwitch( 's5' )


		# Add links
		self.addLink( sHost1, cSwitch )
		self.addLink( sHost2, cSwitch )
		self.addLink( sHost3, cSwitch )
		self.addLink( sHost4, cSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }

#sudo mn --custom topo-LAB02.py --topo mytopo --test pingall