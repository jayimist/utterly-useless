{
  description = "Generic Development Environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";

  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        glfw
        libxkbcommon
        libX11
        wayland
        libglvnd
        mesa
      ];

      shellHook = ''
        export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
          pkgs.libxkbcommon
          pkgs.wayland
          pkgs.glfw
          pkgs.libX11
          pkgs.libglvnd
          pkgs.mesa
        ]}:$LD_LIBRARY_PATH
      '';
    };
  };
}
