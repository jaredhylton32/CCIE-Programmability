from ncclient import manager

# print(capabilities.Capabilities)
device = {'host': '192.168.9.16',
          'username': 'admin',
          'password': 'admin'}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
</filter>"""

with manager.connect(host=device['host'], port=830,
                     username=device['username'],
                     password=device['password'],
                     device_params={'name':'csr'},
                     hostkey_verify=False) as m:

    for capability in m.server_capabilities:
        # print(capability)
        var = 2

    netconf_reply = m.get_config(source='running', filter=netconf_filter)
    print(netconf_reply)
    # done = m.close_session()





"""
with manager.connect(host=host, port=830, username=user, hostkey_verify=False, device_params={'name':'junos'}) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)
"""