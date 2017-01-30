# Ansible role: EPEL

Enables EPEL repository on RedHat/CentOS systems.


## Role Variables

* `epel_repo_url`:
   - Description: URL to EPEL release installation package
   - Default: `https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{ ansible_distribution_major_version }}.noarch.rpm`


## Example Playbook

    - hosts: servers
      roles:
        - { role: viniciusfs.epel }


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
