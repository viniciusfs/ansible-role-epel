# Ansible role: EPEL


[![Build Status](https://travis-ci.org/viniciusfs/ansible-role-epel.svg?branch=master)](https://travis-ci.org/viniciusfs/ansible-role-epel)

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
