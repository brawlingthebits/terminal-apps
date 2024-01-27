import click


class BinaryConverter:
    def __init__(self, binary):
        for i in binary:
            if i not in ["0", "1"]:
                raise ValueError("Binary numbers can only contain 0 or 1")

        if len(binary) > 8:
            raise ValueError("Binary numbers can only be up to 8 digits long")

        self.binary = binary

    def to_decimal(self):
        binary = self.binary[::-1]  # reverse the string
        decimal = 0
        for i in range(len(binary)):
            decimal += int(binary[i])*2**i
        return decimal


@click.command()
@click.option("--binary", prompt="Enter binary number")
def main(binary):
    try:
        BinaryConverter(binary)
        decimal = BinaryConverter(binary).to_decimal()
        click.echo(decimal)
    except ValueError as e:
        click.echo(e)
        return


if __name__ == "__main__":
    main()
