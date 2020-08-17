# Copyright 2020 Codethink Ltd
# Distributed under the terms of the Modified BSD License.

import json
import bz2

from quetz import channel_data
from quetz import repo_data


def update_indexes(dao, pkgstore, channel_name):
    channeldata = channel_data.export(dao, channel_name)
    subdirs = channeldata["subdirs"]

    chandata_json = json.dumps(channeldata, indent=2, sort_keys=True)
    pkgstore.add_file(
        channel_name,
        bz2.compress(chandata_json.encode("utf-8")),
        "channeldata.json.bz2",
    )
    pkgstore.add_file(channel_name, chandata_json, "channeldata.json")

    for dir in subdirs:
        # TODO: generate subdir index.html ?
        repodata = json.dumps(
            repo_data.export(dao, channel_name, dir), indent=2, sort_keys=True
        )
        compressed_repodata = bz2.compress(repodata.encode("utf-8"))
        for fname in ("repodata.json", "current_repodata.json"):
            pkgstore.add_file(
                channel_name, compressed_repodata, f"{dir}/{fname}.bz2"
            )
            pkgstore.add_file(channel_name, repodata, f"{dir}/{fname}")

    # TODO: generate root index.html ?
