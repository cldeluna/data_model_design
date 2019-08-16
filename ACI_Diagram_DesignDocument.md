
<br>
<br>
<br>
<br>
<br>
<br>
<br>
# High Level Design Document
##   Underwater Corporation Software Defined Data Center
<br>
<br>
<br>
Author: **Claudia de Luna**
<br>
Company: _Indigo Wire Networks_
<br>
Email: _claudia@indigowire.net_
<br>
<br>
Date:   2019-08-16 08:26:20.150995
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
![High Level Diagram](./images/Indigo Wire Networks_Final-42high4webex.png)

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## 1. Introduction
<br>
This document will detail the high level design for the new Underwater Corporation Software Defined Data center located in Guadalajara, Mexico in the Marcatel Guadalajara CoLocation buidling at Av. Chapultepec No. 236 Col. Americana, Sector Ju 44160.
<br>
<br>
<br>

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>

## 2. Design Overview
<br>
This is the overview text for the HLD document. This will introduce the HLD Diaagram 
<br>
![High Level Diagram](./ACI_Diagram.png)
<br>
<br>

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>

## 3. Equipment Details
<br>






### Equipment Details for Cisco device Cisco-IOS-XE-native:native

<br>
The primary WAN router, oceana-rtr01, will host the primary 10G circuit to the partner data center.  It will also host the Primary 1G DIA Internet circuit.
<br>
#### General Information
<br>
Model: CSR1000V
<br>
Serial Number: 9YES7U3F0TA
<br>
Hostname: oceana-rtr01
<br>
Software Version: 16.9
<br>
![](images/router.png)
<br>
uwaco.net
<br>
['8.8.8.8']
<br>
#### Interfaces
<br>



GigabitEthernet1
<br>
Description: 
IP Information: {'dhcp': {}}
<br>

GigabitEthernet2
<br>
Description: 
IP Information: {'primary': {'address': '1.1.1.1', 'mask': '255.255.255.0'}}
<br>

GigabitEthernet3
<br>
Description: 
IP Information: {'primary': {'address': '2.2.2.1', 'mask': '255.255.255.0'}}
<br>





Loopback0
<br>
Description: Source Loopback0
IP Information: {'primary': {'address': '192.0.2.1', 'mask': '255.255.255.255'}}
<br>









### Equipment Details for Cisco device Cisco-IOS-XE-native:native

<br>
The secondary WAN router, oceana-rtr02, will host the secondary 10G circuit to the partner data center as well as the secondary DIA Internet circuit (also 1G). 
<br>
#### General Information
<br>
Model: CSR1000V
<br>
Serial Number: 9YES7U3F0TA
<br>
Hostname: oceana-rtr02
<br>
Software Version: 16.9
<br>
![](images/router.png)
<br>
uwaco.net
<br>
['8.8.8.8']
<br>
#### Interfaces
<br>



GigabitEthernet1
<br>
Description: 
IP Information: {'dhcp': {}}
<br>

GigabitEthernet2
<br>
Description: 
IP Information: {'primary': {'address': '2.2.2.1', 'mask': '255.255.255.0'}}
<br>

GigabitEthernet3
<br>
Description: 
IP Information: {'primary': {'address': '3.3.3.1', 'mask': '255.255.255.0'}}
<br>





Loopback0
<br>
Description: Source Loopback0
IP Information: {'primary': {'address': '192.0.2.1', 'mask': '255.255.255.255'}}
<br>










### 3. Details for InternetCloud
<br>
The new data center will support redundant 1G DIA Internet circuits.
<br>



<br>
![key](images/cloud.png)
The Internet










### 3. Details for ACICloud
<br>
The ACI Data Center Fabric will be built out with 4 spines, 12 leafs, and 3 APIC controllers.
<br>



<br>
![key](cisco_images/blue_cloud.png)
ACI Fabric










### 3. Details for ServersStorage
<br>
Server and storage bare metal hosts will be connected directly to the ACI Leafs. ESX Hosts will utilize a combination of VPC and Trunk Uplinks depending on function.  The NetApp storage applicances will utilize Etherchannel/vPC uplinks.
<br>



<br>
![key](cisco_images/PNG/storage server.png)
Servers and Storage





<br>
<br>
<br>
## 4. Conclusion
<br>
This concludes the High Level Design Document
