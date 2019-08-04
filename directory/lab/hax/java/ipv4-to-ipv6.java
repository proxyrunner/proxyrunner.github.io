String ip = "127.0.0.1"; 
String[] octets = ip.split("\\.");
byte[] octetBytes = new byte[4];
 for (int i = 0; i < 4; ++i) {
            octetBytes[i] = (byte) Integer.parseInt(octets[i]);
}

byte ipv4asIpV6addr[] = new byte[16];
ipv4asIpV6addr[10] = (byte)0xff;
ipv4asIpV6addr[11] = (byte)0xff;
ipv4asIpV6addr[12] = octetBytes[0];
ipv4asIpV6addr[13] = octetBytes[1];
ipv4asIpV6addr[14] = octetBytes[2];
ipv4asIpV6addr[15] = octetBytes[3];