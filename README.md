# Solaris-OCI
Open Container Initiative running on Solaris

## Using runc

You should have Solaris 11.4, with solaris-oci brand installed:

### Install the solaris-oci brand

```
$ sudo pkg install system/zones/brand/brand-solaris-oci
```

### Create the python 3.7 virtualenv

```
$ virtualenv-3.7 oci
$ cd oci
$ . bin/activate
```

### Install the package on the virtualenv

```
$ mkdir src
$ cd src
$ git clone -b oci-spec https://github.com/guillermomolina/oci-spec-python.git
$ pip install oci-spec-python
$ git clone https://github.com/guillermomolina/oci-api-python.git
$ pip install oci-api-python
$ git clone https://github.com/guillermomolina/oci-solaris-python.git
$ pip install oci-solaris-python
```

### Create a container (Using standard packages)

```
$ mkdir -p container
$ cd container
$ runc spec
$ sudo mkrootfs .
$ sudo runc run container
@container:~/root$ ^D
$ sudo runc delete container
```

```
$ du -sh rootfs/
1.7G    rootfs/
```

### Using local repo to make smaller containers

```
$ sudo mkrepo
$ mkdir container
$ cd container
$ runc spec
$ sudo mkrootfs -r /var/share/pkg/repositories/solaris-oci .
$ sudo runc run container
@container:~/root$ ^D
$ sudo runc delete container
```

```
$ du -sh rootfs/
49M     rootfs/
```
(Only 49Mb!!!!)

### Run a container

```
$ cd container
$ sudo runc run container
@container:~/root$ ^D
```

### List containers

```
$ runc list
ID            STATUS    BUNDLEPATH         PID
mycontainer   stopped   /zones/container   -1 
```

### Create a container

```
$ cd container
$ sudo runc create container
```

### Start a container

```
$ cd container
$ sudo runc start container
@container:~/root$ ^D
```

### Delete a container

```
$ sudo runc delete container
```
