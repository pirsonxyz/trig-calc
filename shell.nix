# shell.nix
let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      # select Python packages here
      python-pkgs.matplotlib
      python-pkgs.mpmath
      python-pkgs.numpy
      python-pkgs.rich
      python-pkgs.pyqt5
    ]))
  ];
}