from paramiko import SSHClient
client = SSHClient()
client.load_system_host_keys()
client.load_host_keys('~/.ssh/known_hosts')
# client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('192.168.174.130', username='root', password='Ss@56243971')
client.close()
