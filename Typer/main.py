from typing import Optional
import typer
from pathlib import Path

app = typer.Typer()


@app.command("run")
def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher."),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés.")):
    """
    Afficher les fichiers trouvés avec l'extension donnée.
    """

    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()

    if not directory.exists():
        typer.secho(f"Le dossier {directory} n'existe pas", fg=typer.colors.RED)
        raise typer.Exit()

    files = directory.rglob(f"*.{extension}")

    if delete:
        typer.confirm("Voulez-vous vraiment supprimer tous les fichiers trouvés ?", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Suppression du fichier {file}.", fg=typer.colors.RED)
    else:
        typer.secho(f"Fichiers trouvés avec l'extension {extension} :", bg=typer.colors.GREEN, fg=typer.colors.BLACK)
        for file in files:
            typer.secho(file)


@app.command()
def search(extension: str):
    """Chercher les fichiers avec l'extension donnée"""
    main(extension=extension, directory=None, delete=False)


@app.command()
def delete(extension: str):
    """Supprimer les fichiers avec l'extension donnée"""
    main(extension=extension, directory=None, delete=True)


if __name__ == "__main__":
    app()
