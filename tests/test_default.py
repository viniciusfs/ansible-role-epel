import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('servers')


def test_epel_is_installed(Package):
    epel = Package('epel-release')
    assert epel.is_installed
