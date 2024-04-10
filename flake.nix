{
  description = "Odoo flake";

  inputs = {
    nixpkgs.url = "flake:nixpkgs/nixos-23.05";
  };

  outputs = { self, nixpkgs }:
    let
      name = "Python odoo shell";

      systems = [
        "x86_64-linux" # 64bit AMD/Intel x86
        "aarch64-darwin" # 64bit ARM macOS
      ];

      forAllSystems = fn:
        nixpkgs.lib.genAttrs systems
        (system: fn { pkgs = import nixpkgs { inherit system; }; inherit system; });

      pkgs_libjpeg_8d = import (builtins.fetchTarball {
        url = "https://github.com/NixOS/nixpkgs/archive/19f768a97808da4c8700ae24513ab557801be12c.tar.gz";
      }) {};

    in
    {
      packages = forAllSystems({ pkgs, ... }: {
        default = pkgs.stdenv.mkDerivation {
          name = "wkhtmltopdf";

          src = pkgs.fetchurl {
            url = "https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb";
            sha256 = "sha256-20j6GgQzCcS/6Mjg443AbBg/ghWZ3YjU486kfFpdTNM=";
          };

          phases = [ "unpackPhase" "installPhase" ];
          unpackPhase = "${pkgs.dpkg}/bin/dpkg-deb -x $src .";
          installPhase = ''
            mkdir $out
            cp -rv . $out/
          '';

          nativeBuildInputs = [
            pkgs.autoPatchelfHook
          ];

          buildInputs = with pkgs; [
            pkgs_libjpeg_8d.libjpeg_original
            freetype
            xorg.libX11
            xorg.libXrender
            openssl_1_1
            fontconfig
            # libstdc++
            stdenv.cc.cc.lib
          ];
        };
      });

      devShells = forAllSystems ({ pkgs, system }: {
        default = pkgs.mkShell {
          inherit name;
          buildInputs = with pkgs; [
            # Git
            pre-commit

            # Odoo deps for requirements.txt
            cyrus_sasl.dev
            cyrus_sasl
            gsasl
            openldap
            openssl_1_1

            # Python
            python310Packages.libsass
            # python310Packages.pyopenssl
            python310Packages.pip
            # python310Packages.pypdf2
            python310Packages.python-ldap
            python310Packages.setuptools
            python310Packages.virtualenv
            # Python debuggers
            python310Packages.debugpy
            python310Packages.ipdb

            # PostgreSQL
            postgresql_14

            # LSP
            nodePackages.pyright

            # Required for VS Code extensions
            stdenv.cc.cc.lib

            self.packages.${system}.default

          ];

          shellHook = ''
            export PATH=result/local/bin:$PATH
            export PGDATA="$(pwd)/postgres/data/"

            # Required for VS Code extensions, when VS Code from nix shell
            export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
              pkgs.stdenv.cc.cc
            ]}

            if [ -f .venv/bin/activate ]; then
              source .venv/bin/activate
            elif [ -f venv/bin/activate ]; then
              source venv/bin/activate
            elif [ -f .env/bin/activate ]; then
              source .env/bin/activate
            elif [ -f env/bin/activate ]; then
              source env/bin/activate
            fi

            cowsay -t "${name}" | lolcat
          '';
        };
      });
    };
}
