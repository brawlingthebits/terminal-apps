import runpy
from click.testing import CliRunner
from main import BinaryConverter, main


class TestBinaryToDecimal:
    def test_if_binary_is_valid(self):
        binary_input = "010"
        binary_output = BinaryConverter(binary_input)
        decimal_output = binary_output.to_decimal()
        assert decimal_output == 2


class TestClickInteraction:
    runner = CliRunner()

    def test_if_user_can_enter_up_to_eight_digits(self):
        result = self.runner.invoke(main, ["--binary", "10101010"])
        assert result.exit_code == 0

    def test_if_user_cannot_enter_up_to_eight_digits(self):
        result = self.runner.invoke(main, ["--binary", "1010101010"])
        assert "Binary numbers can only be up to 8 digits long" in result.output

    def test_if_user_is_notified_if_number_is_not_binary(self):
        result = self.runner.invoke(main, ["--binary", "101010102"])
        assert "Binary numbers can only contain 0 or 1" in result.output

    def test_if_user_views_the_single_output_field(self):
        result = self.runner.invoke(main, ["--binary", "10101010"])
        assert result.exit_code == 0
        assert result.output == "170\n"
