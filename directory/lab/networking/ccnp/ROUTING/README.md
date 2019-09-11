# 2013 Cisco Systems, Inc. This document is Cisco Public. Page 1

## Implementing Cisco IP Routing (300-101)

# Exam Description: Implementing Cisco IP Routing (ROUTE 300-101)

 is a 120-minute qualifying exam with 50‒60 questions for the Cisco CCNP and CCDP certifications. The ROUTE 300-101 exam certifies the routing knowledge and skills of successful candidates. They are certified in using advanced IP addressing and routing in implementing scalable and highly secure Cisco routers that are connected to LANs, WANs, and IPv6.

The exam also covers the configuration of highly secure routing solutions to support branch offices and mobile workers. The following topics are general guidelines for the content that is likely to be included on the exam. However, other related topics may also appear on any specific version of the exam. To better reflect the contents of the exam and for clarity, the  following guidelines may change at any time without notice.

10% 1.0 Network Principles
1.1 Identify Cisco Express Forwarding concepts
1.1.a FIB
1.1.b Adjacency table
1.2 Explain general network challenges
1.2.a Unicast
1.2.b Out-of-order packets
1.2.c Asymmetric routing
1.3 Describe IP operations
1.3.a ICMP Unreachable and Redirects
1.3.b IPv4 and IPv6 fragmentation
1.3.c TTL
1.4 Explain TCP operations
1.4.a IPv4 and IPv6 (P)MTU
1.4.b MSS
1.4.c Latency
1.4.d Windowing
1.4.e Bandwidth-delay product
1.4.f Global synchronization
1.5 Describe UDP operations
1.5.a Starvation
1.5.b Latency
1.6 Recognize proposed changes to the network
1.6.a Changes to routing protocol parameters
1.6.b Migrate parts of the network to IPv6
1.6.c Routing protocol migration

10% 2.0 Layer 2 Technologies
2.1 Configure and verify PPP
2.1.a Authentication (PAP, CHAP)
2.1.b PPPoE (client side only)
2.2 Explain Frame Relay
2.2.a Operations
2.2.b Point-to-point
2.2.c Multipoint

40% 3.0 Layer 3 Technologies
3.1 Identify, configure, and verify IPv4 addressing and subnetting
3.1.a Address types (Unicast, broadcast, multicast, and VLSM)
3.1.b ARP
3.1.c DHCP relay and server
3.1.d DHCP protocol operations
3.2 Identify IPv6 addressing and subnetting
3.2.a Unicast
3.2.b EUI-64
3.2.c ND, RS/RA
3.2.d Autoconfig (SLAAC)
3.2.e DHCP relay and server
3.2.f DHCP protocol operations
3.3 Configure and verify static routing
3.4 Configure and verify default routing
3.5 Evaluate routing protocol types
3.5.a Distance vector
3.5.b Link state
3.5.c Path vector
3.6 Describe administrative distance
3.7 Troubleshoot passive interfaces
3.8 Configure and verify VRF lite
3.9 Configure and verify filtering with any protocol
3.10 Configure and verify redistribution between any routing protocols or routing sources
3.11 Configure and verify manual and autosummarization with any routing protocol
3.12 Configure and verify policy-based routing
3.13 Identify suboptimal routing
3.14 Explain ROUTE maps
3.15 Configure and verify loop prevention mechanisms
3.15.a Route tagging and filtering
3.15.b Split-horizon
3.15.c Route poisoning
3.16 Configure and verify RIPv2
3.17 Describe RIPng
3.18 Describe EIGRP packet types
3.19 Configure and verify EIGRP neighbor relationship and authentication
3.20 Configure and verify EIGRP stubs
3.21 Configure and verify EIGRP load balancing
3.21.a Equal cost
3.21.b Unequal cost
3.22 Describe and optimize EIGRP metrics
3.23 Configure and verify EIGRP for IPv6
3.24 Describe OSPF packet types
3.25 Configure and verify OSPF neighbor relationship and authentication
3.26 Configure and verify network types, area types, and router types
3.26.a Point-to-point, multipoint, broadcast, nonbroadcast
3.26.b LSA types, area type: backbone, normal, transit, stub, NSSA, totally stub
3.26.c Internal router, backbone router, ABR, ASBR
3.26.d Virtual link
3.27 Configure and verify OSPF path preference
3.28 Configure and verify OSPF operations
3.29 Configure and verify OSPF for IPv6
2013 Cisco Systems, Inc. This document is Cisco Public. Page 4
3.30 Describe, configure, and verify BGP peer relationships and authentication
3.30.a Peer group
3.30.b Active, passive
3.30.c States and timers
3.31 Configure and verify eBGP (IPv4 and IPv6 address families)
3.31.a eBGP
3.31.b 4-byte AS number
3.31.c Private AS
3.32 Explain BGP attributes and best-path selection

10% 4.0 VPN Technologies
4.1 Configure and verify GRE
4.2 Describe DMVPN (single hub)
4.3 Describe Easy Virtual Networking (EVN)

10% 5.0 Infrastructure Security
5.1 Describe IOS AAA using local database
5.2 Describe device security using IOS AAA with TACACS+ and RADIUS
5.2.a AAA with TACACS+ and RADIUS
5.2.b Local privilege authorization fallback
5.3 Configure and verify device access control
5.3.a Lines (VTY, AUX, console)
5.3.b Management plane protection
5.3.c Password encryption
5.4 Configure and verify router security features
5.4.a IPv4 access control lists (standard, extended, time-based)
5.4.b IPv6 traffic filter
5.4.c Unicast reverse path forwarding
20% 6.0 Infrastructure Services
6.1 Configure and verify device management
6.1.a Console and VTY
6.1.b Telnet, HTTP, HTTPS, SSH, SCP
6.1.c (T)FTP
6.2 Configure and verify SNMP
6.2.a v2
6.2.b v3
6.3 Configure and verify logging
6.3.a Local logging, syslog, debugs, conditional debugs
6.3.b Timestamps
2013 Cisco Systems, Inc. This document is Cisco Public. Page 5
6.4 Configure and verify Network Time Protocol (NTP)
6.4.a NTP master, client, version 3, version 4
6.4.b NTP authentication
6.5 Configure and verify IPv4 and IPv6 DHCP
6.5.a DHCP client, IOS DHCP server, DHCP relay
6.5.b DHCP options (describe)
6.6 Configure and verify IPv4 Network Address Translation (NAT)
6.6.a Static NAT, dynamic NAT, PAT
6.7 Describe IPv6 NAT
6.7.a NAT64
6.7.b NPTv6
6.8 Describe SLA architecture
6.9 Configure and verify IP SLA
6.9.a ICMP
6.10 Configure and verify tracking objects
6.10.a Tracking objects
6.10.b Tracking different entities (for example, interfaces, IPSLA results)
6.11 Configure and verify Cisco NetFlow
6.11.a NetFlow v5, v9
6.11.b Local retrieval
6.11.c Export (configuration only)