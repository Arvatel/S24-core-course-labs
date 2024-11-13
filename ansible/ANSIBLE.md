## ansible-playbook ansible/playbooks/dev/main.yaml - result of running the command

```
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Prepare docker] *****************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : include_tasks] *********************************************************************************************************
included: /home/anastasiia/DevOps/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [../../roles/docker : Update pacman cache] ***************************************************************************************************
changed: [localhost]

TASK [../../roles/docker : Install required packages for Docker] **********************************************************************************
ok: [localhost]

TASK [../../roles/docker : Ensure Docker service is started and enabled] **************************************************************************
ok: [localhost]

TASK [../../roles/docker : include_tasks] *********************************************************************************************************
included: /home/anastasiia/DevOps/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [../../roles/docker : Get OS type] ***********************************************************************************************************
changed: [localhost]

TASK [../../roles/docker : Get architecture type] *************************************************************************************************
changed: [localhost]

TASK [../../roles/docker : Install Docker Compose] ************************************************************************************************
changed: [localhost]

PLAY RECAP ****************************************************************************************************************************************
localhost                  : ok=9    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```