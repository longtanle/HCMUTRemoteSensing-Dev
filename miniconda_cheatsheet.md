# Managing environments


1. To create an environment:

```
conda create --name myenv

```

2. To create an environment with a specific version of Python:
```
conda create -n myenv python=3.6
```
3. To create an environment with a specific package:
```
conda create -n myenv scipy
```
OR
```
conda create -n myenv python
conda install -n myenv scipy=0.15.0
```
4. To create an environment with a specific version of Python and multiple packages:
```
    conda create -n myenv python=3.6 scipy=0.15.0 astroid babel
```
