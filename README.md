# Tagbot

Tagbot retags OCI Container Images without needing a full Docker Pull / Docker Push workflow by working directly with the registry API.

## Usage

### Local Usage

```shell
tagbot \
    --username example \
    --password password \
    --source example.azurecr.io/debian:latest \
    --tag v1.0.0
```

This would add an additional tag of `v1.0.0` to `example.azurecr.io/debian:latest`. The container image can then be pulled with either `example.azurecr.io/debian:latest`, or `example.azurecr.io/debian:v1.0.0`

### GitHub Actions Usage

```yaml
name: release

on:
  push:
    tags: ["v[0-9]+.[0-9]+.[0-9]+"]

jobs:
  release:
    name: release
    strategy:
      matrix:
        environment: [staging, production]
    environment:
      name: ${{ matrix.environment }}
    uses: binkhq/tagbot/.github/workflows/retag.yaml@master
      with:
        username: example
        source: example.azurecr.io/${{ github.event.repository.name }}:${{ github.ref_name }}
        tag: v1.0.0
      secrets:
        password: ${{ secrets.ACR_PASSWORD }}
```

## FAQ

* Whats going on with `ghcr.io/binkhq/tagbot`?
  - This still exists, but is formally deprecated and will no longer recieve updates or support
* Are Registries other than Azure Container Registry supported?
  - Azure Container Registry is the only officially supported Registry, but other simple registries like Docker Hub are expected to work just fine.
