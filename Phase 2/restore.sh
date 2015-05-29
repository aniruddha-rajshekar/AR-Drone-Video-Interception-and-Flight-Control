iptables -I INPUT 1 -i wlan1 -m mac --mac-source 34:4d:f7:55:84:1c -j ACCEPT
iptables -I INPUT 1 -i wlan1 -m mac --mac-source 8c:00:6d:40:e4:4f -j ACCEPT
sleep 300
echo "iptable restore"
iptabsles -F
