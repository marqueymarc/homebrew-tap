class Contactsls < Formula
  desc "Read-only viewer for local macOS Contacts"
  homepage "https://github.com/marqueymarc/contactsls"
  url "https://github.com/marqueymarc/contactsls/archive/refs/tags/v1.0.1.tar.gz"
  sha256 "a5bc67fc6c23344a7ffd8887dcabd27c06c427cfb27695579428a37ee178241b"
  license "MIT"

  depends_on "swift" => :build

  def install
    system "swiftc", "-framework", "CoreLocation", "helpers/reverse-geocode.swift", "-o", "reverse-geocode"
    bin.install "contactsls"
    libexec.install "reverse-geocode"
    zsh_completion.install "completions/_contactsls"
  end

  test do
    assert_match "List contacts from local macOS Contacts databases", shell_output("#{bin}/contactsls --help")
  end
end
