# Marc Meyer's Homebrew Tap

## SlideSorter

Install SlideSorter and its Python and ffmpeg dependencies:

```sh
brew install marqueymarc/homebrew-tap/slidesorter
```

Upgrade it later:

```sh
brew update
brew upgrade slidesorter
```

The formula pins a release tag and SHA-256 checksum. A scheduled GitHub Action
checks SlideSorter releases daily and updates the formula when a new stable
release is published. It can also be run manually from the Actions tab.

More about SlideSorter: <https://github.com/marqueymarc/slidesorter>.

## contactsls

Install the read-only macOS Contacts viewer:

```sh
brew install marqueymarc/tap/contactsls
```

It also installs Zsh completion. `--location` reverse-geocodes coordinates
through Apple only when you explicitly request it.

More about contactsls: <https://github.com/marqueymarc/contactsls>.
