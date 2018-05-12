{ buildPythonPackage, pkgs } :

let
  ezdxf = buildPythonPackage rec {
    pname = "ezdxf";
    version = "0.8.8";
    src = pkgs.fetchPypi {
      inherit pname version;
      extension = "zip";
      sha256 = "1bnyg1v4jsnbw7hhfy65h7vxwy91b2vbaavq5j4grb7vjw3ykmzq";
    };
    doCheck = false;

    propagatedBuildInputs = (with pkgs; [
      pyparsing
    ]);
  };

in
  buildPythonPackage rec {
    pname = "survey_fix";
    version = "0.0.2";
    src = ./.;
    doCheck = false;

    propagatedBuildInputs = (with pkgs; [ click ezdxf ]);
  }
