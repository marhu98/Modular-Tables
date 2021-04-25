import click

@click.command()
@click.option("--size","-s",default=500)
def cli(size):
    click.echo("The value of the input was {}".format(size))

if __name__=="__main__":
    cli()
