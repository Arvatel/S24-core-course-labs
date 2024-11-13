# lab 5 task 1
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

## lab 6 task 1

### ansible-playbook ansible/playbooks/pyt/main.yml   

```
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [app_python web app] *************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : include_tasks] *********************************************************************************************************
included: /home/anastasiia/DevOps/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [../../roles/docker : Update pacman cache] ***************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : Install required packages for Docker] **********************************************************************************
ok: [localhost]

TASK [../../roles/docker : Ensure Docker service is started and enabled] **************************************************************************
ok: [localhost]

TASK [../../roles/docker : include_tasks] *********************************************************************************************************
included: /home/anastasiia/DevOps/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [../../roles/docker : Install docker-compose] ************************************************************************************************
ok: [localhost]

TASK [../../roles/web_app : Create a directory if it does not exist] ******************************************************************************
ok: [localhost]

TASK [../../roles/web_app : Move template to destination] *****************************************************************************************
ok: [localhost]

TASK [../../roles/web_app : Run docker-compose] ***************************************************************************************************
[WARNING]: Docker compose: unknown None: /home/anastasiia/DevOps/S24-core-course-labs/ansible/playbooks/pyt/app_python/docker-compose.yml: the
attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
ok: [localhost]

TASK [../../roles/web_app : Stop and remove Docker container] *************************************************************************************
skipping: [localhost]

TASK [../../roles/web_app : Remove directory if it exists] ****************************************************************************************
skipping: [localhost]

TASK [Ensure pip is installed] ********************************************************************************************************************
ok: [localhost]

TASK [Upgrade pip] ********************************************************************************************************************************
ok: [localhost]

TASK [Install Docker via pacman] ******************************************************************************************************************
ok: [localhost]

TASK [Start and enable Docker service] ************************************************************************************************************
ok: [localhost]

PLAY RECAP ****************************************************************************************************************************************
localhost                  : ok=14   changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0 
```