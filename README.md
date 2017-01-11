# EPEL

Enables EPEL repository on RedHat/CentOS systems.

## Role Variables

Name | Description | Default value
-----|-------------|--------------
`epel_repo_url` | URL to EPEL release installation package | `https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{ ansible_distribution_major_version }}.noarch.rpm`
`epel_repo_file` | Path to default EPEL repository file | `/etc/yum.repos.d/epel.repo`


## Example Playbook

    - hosts: servers
      roles:
        - { role: viniciusfs.epel }


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
