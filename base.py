from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def TopoBC():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='172.18.7.0/16')

    
    #Agrega switches
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)


    #Agregando hosts
    h1 = net.addHost('h1', cls=Host, ip='172.18.7.1', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='172.18.7.2', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='172.18.7.3', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='172.18.7.4', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='172.18.7.5', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='172.18.7.6', defaultRoute=None)




    #Agregando links
    net.addLink(s11, s12)
    net.addLink(s12, s13)
    net.addLink(s13, s14)
    net.addLink(s14, s15)
    net.addLink(s11, s10)
    net.addLink(s10, h3)
    net.addLink(s9, h1)
    net.addLink(s9, h2)
    net.addLink(s10, s9)
    net.addLink(s15, h5)
    net.addLink(s15, h6)
    net.addLink(s14, h4)

    #Iniciando red
    net.build()
    #IniciandoControladores
    for controller in net.controllers:
        controller.start()

    #Iniciando switches
    net.get('s14').start([])
    net.get('s13').start([])
    net.get('s10').start([])
    net.get('s12').start([])
    net.get('s11').start([])
    net.get('s15').start([])
    net.get('s9').start([])

    #Enviar configuracion de switches and hosts

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    TopoBC()
