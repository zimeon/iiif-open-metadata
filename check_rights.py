#!/usr/bin/env python3
"""Check rights information in IIIF manifests.

Created 2025-06-04 to inform a presentation at the 2025 IIIF Conference.
https://iiif.io/event/2025/leeds/day1-tuesday/#157

Simeon Warner
"""
import json
import re
import time

import requests


def summarize_dict(title, d):
    """Summarize data based on dictionary with counts.

    Arguments:
        title (str) - String with title of data field collected
        d (dict) - Dictionary with counts
    """
    tot = 0
    for k in d:
        tot += d[k]
    print(f"\n### Summary of {title}:")
    for k in d:
        print("  * %s was %.1f%% (%d)" % (k, 100.0 * d[k] / tot, d[k]))


def fraction(title, count, total):
    """Show count as a fraction of total."""
    print("  * %.1f%% manifests used %s (%d out of %d)" %
          (100.0 * count / total, title, count, total))


class Accumulator():
    """Class to accumulate counts and other information from multiple IIIF implementations."""

    def __init__(self):
        """Initialize Accumulator object."""
        self.manifests = 0
        self.versions = {}
        self.rights = 0
        self.required_statement = 0
        self.see_also = 0

    def add(self, version, rights, required_statement, see_also):
        """Add information for one manifest."""
        self.manifests += 1
        self.versions[version] = self.versions.get(version, 0) + 1
        if rights is not None:
            self.rights += 1
        if required_statement is not None:
            self.required_statement += 1
        if see_also is not None:
            self.see_also += 1

    def summarize(self):
        """Summarize accumulated information."""
        # Summary for all manifests examined
        print("\n## Summary")
        summarize_dict("IIIF versions based on @context", self.versions)
        print("\n### Fractions of manifests using properties")
        fraction("rights", self.rights, self.manifests)
        fraction("requiredStatement", self.required_statement, self.manifests)
        fraction("seeAlso", self.see_also, self.manifests)


def analyze(acc, manifest_json):
    """Analyze one manifest.

    Arguments:
        acc (Accumulator) - object to accumulate results in.
        manifest_json (json) - parsed json object with manfest data.
    """
    version = None
    rights = None
    required_statement = None
    see_also = None
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
    if version == "v2":
        if "attribution" in manifest_json:
            if isinstance(manifest_json["attribution"], str):
                required_statement = 1
            else:
                required_statement = len(manifest_json["attribution"])
    else:  # assume v3
        if "requiredStatement" in manifest_json:
            if isinstance(manifest_json["requiredStatement"], str):
                required_statement = 1
            else:
                required_statement = len(manifest_json["requiredStatement"])
    if "seeAlso" in manifest_json:
        see_also = 1
    # Accumulate totals
    acc.add(version, rights, required_statement, see_also)
    # Summary of this site
    print(f"  * IIIF Version: {version}")
    print(f"  * rights (or license in v2): {rights}")
    print(f"  * requiredStatement (or attribution in v2): {required_statement}")
    print(f"  * seeAlso: {see_also}")


def run_checks():
    """Run check of manifests."""
    acc = Accumulator()
    with open("README.md", "r", encoding="utf-8") as fh:
        heading = ""
        while line := fh.readline():
            if (m := re.match(r"\*\s+(.+)", line)) is not None:
                heading = m.group(1)
            elif (m := re.match(r"  \*\s+(\S+)", line)) is not None:
                time.sleep(1)
                manifest_uri = m.group(1)
                print(f"\n## {heading}")
                print(f"Getting {manifest_uri}...")
                # Data is either a string or parsed JSON
                try:
                    manifest = requests.get(manifest_uri, timeout=60).content
                    manifest_json = json.loads(manifest)
                    # print(json.dumps(manifest_json, indent=2))
                    analyze(acc, manifest_json)
                except Exception as e:  # pylint: disable=broad-exception-caught
                    print(f"```\nLOAD FAILED for {manifest_uri}: " + str(e) + "\n```")
    acc.summarize()


if __name__ == '__main__':
    print("# Manifest rights and requiredStatement checks")
    print("Run at " + time.asctime())
    run_checks()
