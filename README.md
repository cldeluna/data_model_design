Data Model Driven Network Design
=============================================

This repository provides a basic example or proof of concept of network design material driven by configuration payload data in a (relatively) standard data model as discussed in my post, _The Struggle with Structure_ on [The Gratuitous Arp](https://gratuitous-arp.net/).

The intent of this repository is to showcase how a data model driven design process can support the end to end design process by using the configuration payload provided in a structured format to not only drive the configuration but also drive the documentation.

Given a configuration payload (design_cfg_payload.json in this repository), the gen\_design\_doc.py script 
- generates a high level diagram using the pygrapviz module
- generates a design document in Markdown via a Jinja2 template which uses the high level diagram, other icons from a standard library, and the data in the data model to detail the devices in the payload.

I've used the get_data_model_from_device.py script to extract an IOS-XE Cisco DATA Model from a device and use that as a template for all the devices.  I've taken some liberties with the values of some of the fields for expediency.

The script is very tailored to the configuration payload as this was an exercise to see how realistic this new workflow is today.

The [resulting Design Document can be seen here in PDF format](ACI_Diagram_DesignDocument.md).

The script actually generates a [Markdown file which you can see here](ACI_Diagram_DesignDocument.md).

#### Highlights (or maybe Lowlights right now)

The tooling for working with network data models is still in the gestation phase.  To date there is an extremely expensive editor, a JAVA app you can run on Docker, and a plugin for Notepadd++.  I ultimately fell back to working with a text editor.  Until low cost and easy to use tools are out there for this, I believe this will be a big roadblock to adoption.

The YANG models are difficult to use (at least I found them so). That is why I fell back to starting with a Cisco model I pulled from a device.

There is also not alot of training out there on the language itself. DevNet does a nice job with introductory material and helping us to start getting comfortable with the transport (NETCONF and RESTCONF) but if you want to go deeper there isn't much out there on the language itself.  There are some good NANOG presentations but still at a relatively high level. Without tools to help abstract the complexities or training to learn the language, again, adoption is going to be problematic.

##### Automated Diagrams
Automated diagrams have long been a passion of mine and so far one without reward.    

Periodically I dive into this to see if there is anything new and so far I keep falling back to the GraphViz, a dot file, and pygraphviz.  That is what is used in this example.

I'm using LucidChart these days but their API disappoints (you can query but not build last I checked).  
Gephi looked promising but its future is under [discussion](https://gephi.wordpress.com/2018/11/01/is-gephi-obsolete-situation-and-perspectives/).
The python [NetworkX module](https://networkx.github.io) looks interesting but at the end of the day I wind up falling back to pygraphviz.

There is quite alot out there for scientific visualization (NetworkX is one) but nothing quite hits the sweet spot we need for Automated Network Diagrams.

I was excited about the drawing capabilities of Cisco's APIC-EM and actually submitted a feature request to expose the API so that it could be used for drawing but I don't think that went anywhere.




### Requirements

- Jinja2==2.10.1
- MarkupSafe==1.1.1
- pygraphviz==1.5
- requests==2.22.0


### Execution

##### Generate the Design Document

```
(pygraphviz) Claudias-iMac:data_model_design claudia$ python gen_design_doc.py -h
usage: gen_design_doc.py [-h] payload

Script Description

positional arguments:
  payload     Configuration Payload file

optional arguments:
  -h, --help  show this help message and exit

Usage: 'python gen_design_doc.py <design payload>'
(pygraphviz) Claudias-iMac:data_model_design claudia$ 
```


##### Retrieve the Data Model from a Cisco IOS-XE device

The **get\_data\_model\_from_device.py** python script will extract the Cisco IOS XE data model from an IOS XE device.  
This can be tested by bringing up a Cisco 1000Kv or by calling the script against the Cisco DevNet Always On IOS-XE host.

```
python get_data_model_from_device.py -d ios-xe-mgmt.cisco.com -p 9443 -u <username> -w '<password>'
```


```
(pygraphviz) Claudias-iMac:data_model_design claudia$ python get_data_model_from_device.py -h
usage: get_data_model_from_device.py [-h] [-d DEVICE] [-p PORT] [-u USERNAME]
                                     [-w PASSWORD]

Script Description

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE, --device DEVICE
                        Device to query
  -p PORT, --port PORT  Port
  -u USERNAME, --username USERNAME
                        Username for device
  -w PASSWORD, --password PASSWORD
                        Password for device

Usage: ' python get_data_model_from_device.py'
(pygraphviz) Claudias-iMac:data_model_design claudia$ 

```


My gratitude to Mike Griffin!

[graphviz tutorial blog post](https://mikegriffin.ie/blog/20110308-a-graphviz-tutorial).

