# rabbit

```
ls -l|awk '/^d/ {print $NF}'| xargs -I {} echo mkdir {}
```