#!/usr/bin/env python3
"""Refresh the contactsls formula from a tagged GitHub release."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen


OWNER = "marqueymarc"
REPOSITORY = "contactsls"
FORMULA = Path(__file__).parents[1] / "Formula" / "contactsls.rb"


def download(url: str) -> bytes:
    request = Request(url, headers={"Accept": "application/vnd.github+json"})
    with urlopen(request, timeout=60) as response:
        return response.read()


def latest_release() -> tuple[str, str]:
    release = json.loads(download(f"https://api.github.com/repos/{OWNER}/{REPOSITORY}/releases/latest"))
    tag = str(release["tag_name"])
    if not tag.startswith("v") or len(tag) == 1:
        raise ValueError(f"Unexpected release tag: {tag!r}")
    source_url = f"https://github.com/{OWNER}/{REPOSITORY}/archive/refs/tags/{tag}.tar.gz"
    return tag, hashlib.sha256(download(source_url)).hexdigest()


def write_formula(tag: str, checksum: str) -> None:
    if not tag.startswith("v") or len(tag) == 1:
        raise ValueError(f"Unexpected release tag: {tag!r}")
    if len(checksum) != 64 or any(character not in "0123456789abcdef" for character in checksum.lower()):
        raise ValueError("Expected a SHA-256 checksum")
    source_url = f"https://github.com/{OWNER}/{REPOSITORY}/archive/refs/tags/{tag}.tar.gz"
    FORMULA.write_text(
        f'''class Contactsls < Formula
  desc "Read-only viewer for local macOS Contacts"
  homepage "https://github.com/{OWNER}/{REPOSITORY}"
  url "{source_url}"
  sha256 "{checksum}"
  license "MIT"

  depends_on "swift" => :build

  def install
    system "swiftc", "-framework", "CoreLocation", "helpers/reverse-geocode.swift", "-o", "reverse-geocode"
    bin.install "contactsls"
    libexec.install "reverse-geocode"
    zsh_completion.install "completions/_contactsls"
  end

  test do
    assert_match "List contacts from local macOS Contacts databases", shell_output("#{{bin}}/contactsls --help")
  end
end
''',
        encoding="utf-8",
    )


def main() -> None:
    tag, checksum = (sys.argv[1], sys.argv[2]) if len(sys.argv) == 3 else latest_release()
    write_formula(tag, checksum)
    print(f"Updated contactsls {tag.removeprefix('v')} ({checksum})")


if __name__ == "__main__":
    main()
