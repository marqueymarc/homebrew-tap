#!/usr/bin/env python3
"""Refresh the SlideSorter formula from the latest public GitHub release."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen


OWNER = "marqueymarc"
REPOSITORY = "slidesorter"
FORMULA = Path(__file__).parents[1] / "Formula" / "slidesorter.rb"


def download(url: str) -> bytes:
    request = Request(url, headers={"Accept": "application/vnd.github+json"})
    with urlopen(request, timeout=60) as response:
        return response.read()


def main() -> None:
    release = json.loads(download(f"https://api.github.com/repos/{OWNER}/{REPOSITORY}/releases/latest"))
    tag = str(release["tag_name"])
    if not tag.startswith("v") or len(tag) == 1:
        raise ValueError(f"Unexpected release tag: {tag!r}")
    version = tag.removeprefix("v")
    source_url = f"https://github.com/{OWNER}/{REPOSITORY}/archive/refs/tags/{tag}.tar.gz"
    checksum = hashlib.sha256(download(source_url)).hexdigest()
    FORMULA.write_text(
        f'''class Slidesorter < Formula
  include Language::Python::Virtualenv

  desc "Local-first, recoverable photo and video review"
  homepage "https://github.com/{OWNER}/{REPOSITORY}"
  url "{source_url}"
  sha256 "{checksum}"
  license "MIT"

  depends_on "ffmpeg"
  depends_on "python@3.13"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "SlideSorter #{{version}}", shell_output("#{{bin}}/slidesorter --version")
  end
end
''',
        encoding="utf-8",
    )
    print(f"Updated SlideSorter {version} ({checksum})")


if __name__ == "__main__":
    main()
