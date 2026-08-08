class Slidesorter < Formula
  include Language::Python::Virtualenv

  desc "Local-first, recoverable photo and video review"
  homepage "https://github.com/marqueymarc/slidesorter"
  url "https://github.com/marqueymarc/slidesorter/archive/refs/tags/v3.9.5.tar.gz"
  sha256 "fbd4261ce39d2cdb769fe2c0319c8056f536e02c28bf291724782cf0fe0d05ce"
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
