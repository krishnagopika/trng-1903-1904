# Lecture Plan

1. Ansible

---


# Ansible

- used to automate tasks like provisioning, configuration management, continious delivery, security compliance and application management in multiple servers
- simple, hybrid, powerfull, agentless, idempotent and community driven

**provisioning**

- vpc with 3 vms
- host: vms
- Intentory : set of hosts ansible works with
- pattern: catrgorizations of vms

**config management**

- configure os patches
- installing service to vm

**agentless**

- ansible uses ssh to run the taks in the vm
- awx or ansible tower: a grapical interface to run ansible

### Playbooks

- set of plays (tasks)
- play: name, host, task
- roles: used to group and reuse tasks
- collections are available in ansible galaxy

**modules**: small programs that perform actions on hosts

    - task
    - play
    - playbook
    - role
    - collections


### variables


- used to pass dynamic values to the playbooks

**types**

1. simple variables

2. boolean

3. list variables

ex: 

```
region
    - us-east-1
```
4. map variables

```

tags:
    name: value

```


**dynamic inventory:** dynamic hosts (vms or local servers) 


**[best practices](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html#best-practices)**













