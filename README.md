# ProyectoNWSL
Implementacion de la emulación de una red lan y parámetros de medición en el software mininet de acuerdo a las siguientes indicaciones::
1.	Inicie mininiet
2.	Implemente la topología*
3.	Haga ping entre todos los hosts
*La topología debe incluir los anchos de banda y retardo por enlace indicados.

                    172.18.7.0/16

 +          [SW]------------[SW]------------[SW]
 +            |               |               |
 + [HS]------[SW]+           +[SW]           +[SW]------[HS]
 +           |               |               |
 +          [SW]            [SW]            [SW]
 +        /     \          /    \          /    \  
 +    [HS]+     +[HS]   +[HS]    +[HS]   [HS]    +[HS]
