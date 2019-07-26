# Tagbot

Tagbot retags OCI Container Images without needing a full Docker Pull / Docker Push style workflow by working directly with the registry API.

We use this as part of our image promotion workflow between our Staging and Production environments.

## Usage

```shell
tagbot \
    --username example \
    --password password \
    --source example.azurecr.io/battlestar:apollo \
    --tag starbuck
```

This would add an additional tag of `starbuck` to `example.azurecr.io/battlestar:apollo`. The container image can then be pulled with either `example.azurecr.io/battlestar:starbuck`, or `example.azurecr.io/battlestar:apollo`

# TODO

* Rewrite in Go
