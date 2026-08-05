class Slidesorter < Formula
  include Language::Python::Virtualenv

  desc "Local-first, recoverable photo and video review"
  homepage "https://github.com/marqueymarc/slidesorter"
  url "https://github.com/marqueymarc/slidesorter/archive/refs/tags/v3.8.0.tar.gz"
  sha256 "8f70634e032c3aac38090e85bf7ec62b083f2180d711d6540c72b1a466aeaebe"
  license "MIT"

  depends_on "ffmpeg"
  depends_on "python@3.13"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "SlideSorter #{version}", shell_output("#{bin}/slidesorter --version")
  end
end
