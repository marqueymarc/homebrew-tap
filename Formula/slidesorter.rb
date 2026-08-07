class Slidesorter < Formula
  include Language::Python::Virtualenv

  desc "Local-first, recoverable photo and video review"
  homepage "https://github.com/marqueymarc/slidesorter"
  url "https://github.com/marqueymarc/slidesorter/archive/refs/tags/v3.9.1.tar.gz"
  sha256 "7aca675ca0172f440b2d1d666aecc017d67dd7dcf198189eb82af17b6a1f9e5a"
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
