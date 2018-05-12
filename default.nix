with import <nixpkgs> {};

let
  survey_fix = pkgs.callPackage ./release.nix {
    pkgs = pkgs.python3.pkgs;
    buildPythonPackage = pkgs.python3.pkgs.buildPythonPackage;
  };
in (pkgs.python3.withPackages (_: [survey_fix]))
