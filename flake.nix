# flake.nix
{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    /*poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };*/
  };


  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pythonPkgs = pkgs.python310Packages;
        system = "x86_64-linux";
        pkgs = nixpkgs.legacyPackages.${system};
        fhs = pkgs.buildFHSUserEnv {
          name = "mainline_shell";
          targetPkgs = pkgs: (with pkgs; [
            #poetry
            python310
            pythonPkgs.pip
            ta-lib
            stdenv.cc.cc.lib
            #binutils
            libz
            graphviz
            glibc
            gnumake clang boost pkg-config cmake
            nodejs
          ]);
          #extraBuildCommandsMulti="pip install poetry";
          #extraBuildCommands="pip";
          #extraInstallCommands="pip install numpy";
          profile = ''
            export CFLAGS="-I/usr/include $CFLAGS"
            export LDFLAGS="-L/usr/lib $LDFLAGS"
            export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/lib"
            #source "$( poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate"
            #POETRY_ENV_PATH=$(poetry env list --full-path | grep Activated | cut -d' ' -f1)
            #if [ -n "$POETRY_ENV_PATH" ]; then
            #  echo "Activating poetry environment"
            #  source "$POETRY_ENV_PATH/bin/activate"
            #else
            #  echo "No active poetry environment found"
            #fi
            #poetry env use $(which python)
            #bash -C poetry shell
            echo "load .env file"
            if [ -f ./.env ]; then
              set -a  # automatically export all variables
              source ./.env
              set +a
            fi
          '';
          #runScript = pkgs.writeScript "init.sh" ''
          runScript = "fish";
        };
      in
      {
        devShells.default = fhs.env;

        /*packages = {
          myapp = mkPoetryApplication { projectDir = self; };
          default = self.packages.${system}.myapp;
        };*/
      }
      );
}