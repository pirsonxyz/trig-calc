let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.matplotlib
      python-pkgs.mpmath
      python-pkgs.numpy
      python-pkgs.rich
      python-pkgs.pyqt5
    ]))
  ];
  shellHook = ''
    echo "Bienvenido a Trig Calc!"
  '';
}