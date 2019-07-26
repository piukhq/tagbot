#!/usr/bin/env python3

import re

import click
import requests


@click.command()
@click.option("--username", required=True, help="Username for Container Registry")
@click.option("--password", required=True, help="Password for Container Registry")
@click.option("--source", required=True, help="Source Container Image")
@click.option("--tag", required=True, help="New Container Image Tag")
def tag(username, password, source, tag):
    s = re.split("[:/]", source)

    print(f"Tagging {s[0]}/{s[1]}:{tag} to {s[0]}/{s[1]}:{s[2]}")

    source_image = requests.get(
        f"https://{s[0]}/v2/{s[1]}/manifests/{s[2]}",
        headers={"Accept": "application/vnd.docker.distribution.manifest.v2+json"},
        auth=(username, password),
    )

    source_image.raise_for_status()

    requests.put(
        f"https://{s[0]}/v2/{s[1]}/manifests/{tag}",
        headers={"Content-Type": "application/vnd.docker.distribution.manifest.v2+json"},
        auth=(username, password),
        data=(source_image.text),
    ).raise_for_status()


if __name__ == "__main__":
    tag()
