{
  description = "Odoo flake";

  inputs = {
    nixpkgs.url = "flake:nixpkgs/nixos-23.05";
  };

  outputs = inputs:
    let
      pkgs = inputs.nixpkgs.legacyPackages.x86_64-linux;
      name = "Python odoo shell";

      systems = [
        "x86_64-linux" # 64bit AMD/Intel x86
        "aarch64-darwin" # 64bit ARM macOS
      ];

      forAllSystems = fn:
        inputs.nixpkgs.lib.genAttrs systems
        (system: fn { pkgs = import inputs.nixpkgs { inherit system; }; });

    in
    {
      devShells = forAllSystems ({ pkgs }: {
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
          ];

          shellHook = ''
            export PATH=result/local/bin:$PATH
            export PGDATA="$(pwd)/postgres/data/"

            # Required for VS Code extensions, when VS Code from nix shell
            export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
              pkgs.stdenv.cc.cc
            ]}

            echo "${name}" | cowsay | lolcat
          '';
        };
      });
    };
}
