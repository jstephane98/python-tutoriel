import typer


# app = typer.Typer()


def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"),
         extension: str = typer.Argument("txt", help="Extension du fichier à rechercher")):
    """
    Affiche les fichiers avec l'extension donnée.
    """

    # typer.echo(f"Recherche des fichiers avec l'extension {extension}.")
    # ext = typer.prompt(f"Quelle extension souhaitez-vous rechercher?")
    # print(ext)

    # if delete:
    #     confirm = typer.confirm("Souhaitez vous vraiment supprimer les fichiers ?")
    #     if not confirm:
    #         typer.echo("On annule l'opération")
    #         raise typer.Abort()
    #
    #     print("Suppression des fichiers.")

    # Style with Typer
    # extension = typer.style(extension, fg=typer.colors.BLUE)
    # print(f"Extension {extension}, Suppression: {delete}")

    # Progress Bar
    # numbers = range(100)
    # with typer.progressbar(numbers) as progress:
    #     for _ in progress:
    #         time.sleep(1)
    #
    # typer.echo("Fin du programme .")


# @app.command()
# def search_py():
#     main(delete=True, extension="py")
#
#
# @app.command()
# def delete_py():
#     main(delete=True, extension="py")


if __name__ == '__main__':
    typer.run(main)
    # app()
