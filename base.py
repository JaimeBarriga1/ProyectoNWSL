Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        #Inicia topology
        Topo.__init__( self )

      # Add hosts
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftDownOneHost = self.addHost( 'h4' )
        leftDownSecondHost = self.addHost( 'h6' )
        rightDownOneHost = self.addHost( 'h5' )
        rightDownSecondHost = self.addHost( 'h7' )

        #Add Switches
        leftSwitch = self.addSwitch( 's1' )
        centerSwitch = self.addSwitch( 's2' )
        rightSwitch = self.addSwitch( 's3' )
        leftCenterSwitch = self.addSwitch( 's4' )
        leftDownSwitch = self.addSwitch( 's5' )
        rightCenterSwitch = self.addSwitch( 's6' )
        rightDownSwitch = self.addSwitch( 's7' )

        # Agrega links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }
