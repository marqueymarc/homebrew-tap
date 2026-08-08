class Slidesorter < Formula
  include Language::Python::Virtualenv

  desc "Local-first, recoverable photo and video review"
  homepage "https://github.com/marqueymarc/slidesorter"
  url "https://github.com/marqueymarc/slidesorter/archive/refs/tags/v3.9.3.tar.gz"
  sha256 "452b2b791bf6df3e8fe3a57fbb579ba87f15e3fd6dbbe85bcfbd7227c6de0017"
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
