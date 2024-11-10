## Terraform show

```
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "aaa928dbecc5"
    id                                          = "aaa928dbecc5ee6754136d5ae25bf7ef8f8c9a5676dcfd108ab03bd0111ad815"
    image                                       = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx"
    image_id     = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb"
}


Outputs:

container_id = "aaa928dbecc5ee6754136d5ae25bf7ef8f8c9a5676dcfd108ab03bd0111ad815"
image_id = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx"
```

## terraform state list
```
docker_container.nginx
docker_image.nginx
```

## terraform apply (after changing external port from 8000 to 8080)

```
docker_image.nginx: Refreshing state... [id=sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx]
docker_container.nginx: Refreshing state... [id=aaa928dbecc5ee6754136d5ae25bf7ef8f8c9a5676dcfd108ab03bd0111ad815]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "aaa928dbecc5" -> (known after apply)
      ~ id                                          = "aaa928dbecc5ee6754136d5ae25bf7ef8f8c9a5676dcfd108ab03bd0111ad815" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "tutorial"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)
      - network_mode                                = "bridge" -> null # forces replacement
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (20 unchanged attributes hidden)

      ~ healthcheck {
          + attach                                      = (known after apply)
          + bridge                                      = (known after apply)
          + cgroupns_mode                               = (known after apply)
          + command                                     = (known after apply)
          + container_logs                              = (known after apply)
          + container_read_refresh_timeout_milliseconds = (known after apply)
          + cpu_set                                     = (known after apply)
          + cpu_shares                                  = (known after apply)
          + destroy_grace_seconds                       = (known after apply)
          + dns                                         = (known after apply)
          + dns_opts                                    = (known after apply)
          + dns_search                                  = (known after apply)
          + domainname                                  = (known after apply)
          + entrypoint                                  = (known after apply)
          + env                                         = (known after apply)
          + exit_code                                   = (known after apply)
          + gpus                                        = (known after apply)
          + group_add                                   = (known after apply)
          + hostname                                    = (known after apply)
          + id                                          = (known after apply)
          + image                                       = (known after apply)
          + init                                        = (known after apply)
          + ipc_mode                                    = (known after apply)
          + log_driver                                  = (known after apply)
          + log_opts                                    = (known after apply)
          + logs                                        = (known after apply)
          + max_retry_count                             = (known after apply)
          + memory                                      = (known after apply)
          + memory_swap                                 = (known after apply)
          + must_run                                    = (known after apply)
          + name                                        = (known after apply)
          + network_data                                = (known after apply)
          + network_mode                                = (known after apply)
          + pid_mode                                    = (known after apply)
          + privileged                                  = (known after apply)
          + publish_all_ports                           = (known after apply)
          + read_only                                   = (known after apply)
          + remove_volumes                              = (known after apply)
          + restart                                     = (known after apply)
          + rm                                          = (known after apply)
          + runtime                                     = (known after apply)
          + security_opts                               = (known after apply)
          + shm_size                                    = (known after apply)
          + start                                       = (known after apply)
          + stdin_open                                  = (known after apply)
          + stop_signal                                 = (known after apply)
          + stop_timeout                                = (known after apply)
          + storage_opts                                = (known after apply)
          + sysctls                                     = (known after apply)
          + tmpfs                                       = (known after apply)
          + tty                                         = (known after apply)
          + user                                        = (known after apply)
          + userns_mode                                 = (known after apply)
          + wait                                        = (known after apply)
          + wait_timeout                                = (known after apply)
          + working_dir                                 = (known after apply)
        } -> (known after apply)

      ~ labels {
          + attach                                      = (known after apply)
          + bridge                                      = (known after apply)
          + cgroupns_mode                               = (known after apply)
          + command                                     = (known after apply)
          + container_logs                              = (known after apply)
          + container_read_refresh_timeout_milliseconds = (known after apply)
          + cpu_set                                     = (known after apply)
          + cpu_shares                                  = (known after apply)
          + destroy_grace_seconds                       = (known after apply)
          + dns                                         = (known after apply)
          + dns_opts                                    = (known after apply)
          + dns_search                                  = (known after apply)
          + domainname                                  = (known after apply)
          + entrypoint                                  = (known after apply)
          + env                                         = (known after apply)
          + exit_code                                   = (known after apply)
          + gpus                                        = (known after apply)
          + group_add                                   = (known after apply)
          + hostname                                    = (known after apply)
          + id                                          = (known after apply)
          + image                                       = (known after apply)
          + init                                        = (known after apply)
          + ipc_mode                                    = (known after apply)
          + log_driver                                  = (known after apply)
          + log_opts                                    = (known after apply)
          + logs                                        = (known after apply)
          + max_retry_count                             = (known after apply)
          + memory                                      = (known after apply)
          + memory_swap                                 = (known after apply)
          + must_run                                    = (known after apply)
          + name                                        = (known after apply)
          + network_data                                = (known after apply)
          + network_mode                                = (known after apply)
          + pid_mode                                    = (known after apply)
          + privileged                                  = (known after apply)
          + publish_all_ports                           = (known after apply)
          + read_only                                   = (known after apply)
          + remove_volumes                              = (known after apply)
          + restart                                     = (known after apply)
          + rm                                          = (known after apply)
          + runtime                                     = (known after apply)
          + security_opts                               = (known after apply)
          + shm_size                                    = (known after apply)
          + start                                       = (known after apply)
          + stdin_open                                  = (known after apply)
          + stop_signal                                 = (known after apply)
          + stop_timeout                                = (known after apply)
          + storage_opts                                = (known after apply)
          + sysctls                                     = (known after apply)
          + tmpfs                                       = (known after apply)
          + tty                                         = (known after apply)
          + user                                        = (known after apply)
          + userns_mode                                 = (known after apply)
          + wait                                        = (known after apply)
          + wait_timeout                                = (known after apply)
          + working_dir                                 = (known after apply)
        } -> (known after apply)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id = "aaa928dbecc5ee6754136d5ae25bf7ef8f8c9a5676dcfd108ab03bd0111ad815" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=aaa928dbecc5ee6754136d5ae25bf7ef8f8c9a5676dcfd108ab03bd0111ad815]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=24fea2bcfca458a30affcca117110d7ebfd57b522a41961bd069c2d7f0785b02]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "24fea2bcfca458a30affcca117110d7ebfd57b522a41961bd069c2d7f0785b02"
image_id = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx"
```

## terraform show (after change)

```
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "24fea2bcfca4"
    id                                          = "24fea2bcfca458a30affcca117110d7ebfd57b522a41961bd069c2d7f0785b02"
    image                                       = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx"
    image_id     = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb"
}


Outputs:

container_id = "24fea2bcfca458a30affcca117110d7ebfd57b522a41961bd069c2d7f0785b02"
image_id = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx"
```

## changed container name
```
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
559b1e087def   3b25b682ea82   "/docker-entrypoint.…"   3 seconds ago   Up 3 seconds   0.0.0.0:8080->80/tcp   ContainerName
```
## terraform state show docker_container.nginx 

```

# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "559b1e087def"
    id                                          = "559b1e087def271294cddd0026a4160d12d2d583610453213320adabec59700a"
    image                                       = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "ContainerName"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```

## terraform state show 

```
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx"
    image_id     = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb"
}
```

## terraform output

```
container_id = "559b1e087def271294cddd0026a4160d12d2d583610453213320adabec59700a"
image_id = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx"
```