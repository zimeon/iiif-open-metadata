#!/usr/bin/env python3
"""
"""
import json
import re
import requests
import time


def summarize(title, d):
    tot = 0
    for k in d:
        tot += d[k]
    print(f"Summary of {title}:")
    for k in d:
        print("   %s was %.1f%% (%d)" % (k, 100.0*d[k]/tot, d[k]))


def fraction(title, count, total):
    print("%.1f%% manifests used %s (%d out of %d)" % (100.0*count/total, title, count, total))


manifests = 0
versions = {}
with_attribution = 0
with_rights = 0
with_required_statement = 0

with open("README.md", "r") as fh:
    while line := fh.readline():
        if (m := re.match(r"  \*\s+(\S+)", line)) is not None:
            time.sleep(1)
            manifest_uri = m.group(1)
            print(f"\nGetting {manifest_uri}...")
            # Data is either a string or parsed JSON
            manifest = requests.get(manifest_uri).content
            manifest_json = json.loads(manifest)
            # print(json.dumps(manifest_json, indent=2))
            version = None
            attribution = None
            required_statement = None
            rights = None
            if "@context" in manifest_json:
                if not isinstance(manifest_json["@context"], str):
                    if "http://iiif.io/api/presentation/3/context.json" in manifest_json["@context"]:
                        version = "v3"
                    else:
                        # @context shouldn't be an array in v2
                        version = "bad array @context"
                elif manifest_json["@context"] == "http://iiif.io/api/presentation/2/context.json":
                    version = "v2"
                elif manifest_json["@context"] == "https://iiif.io/api/presentation/2/context.json":
                    version = "v2"
                    print("BAD https @context %s" % (manifest_json["@context"]))
                elif manifest_json["@context"] == "http://iiif.io/api/presentation/3/context.json":
                    version = "v3"
                elif manifest_json["@context"] == "https://iiif.io/api/presentation/3/context.json":
                    print("BAD https @context %s" % (manifest_json["@context"]))
                    version = "v3"
                else:
                    version = manifest_json["@context"]
            if version == "v2":
                if "license" in manifest_json:
                    rights = manifest_json["license"]
            else:  # assume v3
                if "rights" in manifest_json:
                    rights = manifest_json["rights"]
            if "attribution" in manifest_json:
                if isinstance(manifest_json["attribution"], str):
                    attribution = 1
                else:
                    attribution = len(manifest_json["attribution"])
            if "requiredStatement" in manifest_json:
                if isinstance(manifest_json["requiredStatement"], str):
                    required_statement = 1
                else:
                    required_statement = len(manifest_json["requiredStatement"])
            # Accumulate totals
            manifests += 1
            versions[version] = versions.get(version, 0) + 1
            if rights is not None:
                with_rights += 1
            if attribution is not None:
                with_attribution += 1
            if required_statement is not None:
                with_required_statement += 1
            # Summary of this site
            print(f"IIIF Version: {version}")
            print(f"rights (or license in v2): {rights}")
            print(f"attribution: {attribution}")
            print(f"requiredStatement: {required_statement}")
# Summary for all manifests examined
summarize("versions", versions)
fraction("rights", with_rights, manifests)
fraction("attribution", with_attribution, manifests)
fraction("requiredStatement", with_required_statement, manifests)
