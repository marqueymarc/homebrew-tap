class Slidesorter < Formula
  include Language::Python::Virtualenv

  desc "Local-first, recoverable photo and video review"
  homepage "https://github.com/marqueymarc/slidesorter"
  url "https://github.com/marqueymarc/slidesorter/archive/refs/tags/v3.7.0.tar.gz"
  sha256 "7ca71626fac140d1240f5a4c6a83abe260676ce6e9a698f0ef3801a166360de1"
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
