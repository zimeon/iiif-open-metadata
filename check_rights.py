#!/usr/bin/env python3
"""
"""
import json
import re
import requests
import time


with open("README.md", "r") as fh:
    while line := fh.readline():
        if (m := re.match(r"\s+\*\s+(\S+)", line)) is not None:
            time.sleep(1)
            manifest_uri = m.group(1)
            print(f"Getting {manifest_uri}...")
            # Data is either a string or parsed JSON
            manifest = requests.get(manifest_uri).content
            manifest_json = json.loads(manifest)
            # print(json.dumps(manifest_json, indent=2))
            version = None
            attribution = None
            manifest_rights = None
            if "@context" in manifest_json:
                if manifest_json["@context"] == "http://iiif.io/api/presentation/2/context.json":
                    version = 2
                elif manifest_json["@context"] == "http://iiif.io/api/presentation/3/context.json":
                    version = 3
                else:
                    version = manifest_json["@context"]
            if version == 2:
                if "license" in manifest_json:
                    manifest_rights = manifest_json["license"]
                    if not isinstance(manifest_rights, str):
                        manifest_rights = manifest_rights[0]
            else:  # assume 3
                if "rights" in manifest_json:
                    manifest_rights = manifest_json.rights
            if "attribution" in manifest_json:
                if isinstance(manifest_json["attribution"], str):
                    attribution = 1
                else:
                    attribution = len(manifest_json["attribution"])
            print(f"Version: {version}")
            print(f"Manifest rights: {manifest_rights}")
            print(f"Attributions: {attribution}")
            print()
