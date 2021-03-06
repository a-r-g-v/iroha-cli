import unittest
import sys, os

sys.path.insert(0, os.path.abspath(__file__ + "/../../cli"))
sys.path.insert(0, os.path.abspath(__file__ + "/../../schema"))
from cli import commands
from cli.exception import CliException


class Sample:
    def __init__(self):
        self.sample_account_id_1 = "sample_account_id_1"
        self.sample_account_id_2 = "sample_account_id_2"
        self.sample_account_id_3 = "sample_account_id_3"

        self.sample_asset_id_1 = "sample_asset_id_1"
        self.sample_asset_id_2 = "sample_asset_id_2"
        self.sample_asset_id_3 = "sample_asset_id_3"

        self.sample_account_name = "sonoko_mizuki"

        self.sample_domain_id = "japan"
        self.sample_account_name = "mizuki"
        self.sample_keypair_path = "mizuki_key"

class TestAddAssetQuantity(unittest.TestCase):

    def setUp(self):
        self.commands = commands.CommandList().commands
        self.sample = Sample()

    def test_normal_command_generate(self):
        command = self.commands["AddAssetQuantity"]["function"](
            {"account_id": self.sample.sample_account_id_1,
             "asset_id": self.sample.sample_asset_id_1,
             "amount": 10.0
             }
        )
        self.assertTrue(command.add_asset_quantity)
        self.assertTrue(command.add_asset_quantity.account_id == self.sample.sample_account_id_1)
        self.assertTrue(command.add_asset_quantity.asset_id == self.sample.sample_asset_id_1)
        self.assertTrue(command.add_asset_quantity.amount.value.first == 10)

    def test_no_account_id_command_generate(self):
        try:
            self.commands["AddAssetQuantity"]["function"](
                {
                    "asset_id": self.sample.sample_asset_id_1,
                    "amount": 10.0
                }
            )
        except CliException as e:
            self.assertTrue(e.args[0] == "account_id is required")
        else:
            self.fail("I want to CliException")

    def test_no_asset_id_command_generate(self):
        try:
            self.commands["AddAssetQuantity"]["function"](
                {
                    "account_id": self.sample.sample_account_id_1,
                    "amount": 10.0
                }
            )
        except CliException as e:
            self.assertTrue(e.args[0] == "asset_id is required")
        else:
            self.fail("I want to exception")

    def test_no_amount_command_generate(self):
        try:
            self.commands["AddAssetQuantity"]["function"](
                {
                    "account_id": self.sample.sample_account_id_1,
                    "asset_id": self.sample.sample_asset_id_1
                }
            )
        except CliException as e:
            self.assertTrue(e.args[0] == "amount is required")
        else:
            self.fail("I want to exception")

    def test_not_str_account_id_command_generate(self):
        try:
            self.commands["AddAssetQuantity"]["function"](
                {
                    "account_id": 123,
                    "asset_id": self.sample.sample_asset_id_1,
                    "amount": 10.0
                }
            )
        except CliException as e:
            self.assertTrue(e.args[0] == "account_id is <class 'str'>")
        else:
            self.fail("I want to exception")

    def test_not_str_amount_id_command_generate(self):
        try:
            self.commands["AddAssetQuantity"]["function"](
                {
                    "account_id": self.sample.sample_account_id_1,
                    "asset_id": self.sample.sample_asset_id_1,
                    "amount": 100
                }
            )
        except CliException as e:
            self.assertTrue(e.args[0] == "amount is <class 'float'>")
        else:
            self.fail("I want to exception")

class TestCreateAccount(unittest.TestCase):

    def setUp(self):
        self.commands = commands.CommandList().commands
        self.sample = Sample()

    def tearDown(self):
        base = self.sample.sample_account_name + "@" + self.sample.sample_domain_id
        base_key = self.sample.sample_keypair_path
        if os.path.exists(base + ".pub"):
            os.remove(base + ".pub")
            os.remove(base + ".pri")
        if os.path.exists(base_key + ".pub"):
            os.remove(base_key + ".pub")
            os.remove(base_key + ".pri")

    def test_normal_no_keypair_command_generate(self):
        command = self.commands["CreateAccount"]["function"](
            {"account_name": self.sample.sample_account_name,
             "domain_id": self.sample.sample_domain_id
             }
        )
        self.assertTrue(command.create_account)
        self.assertTrue(command.create_account.account_name == self.sample.sample_account_name)
        self.assertTrue(command.create_account.domain_id == self.sample.sample_domain_id)
        kaypair_name = self.sample.sample_account_name +"@"+ self.sample.sample_domain_id
        self.assertTrue(os.path.exists(kaypair_name+".pub") and os.path.exists(kaypair_name+".pri"))

    def test_normal_command_generate(self):
        command = self.commands["CreateAccount"]["function"](
            {"account_name": self.sample.sample_account_name,
             "domain_id": self.sample.sample_domain_id,
             "keypair_name": self.sample.sample_keypair_path
             }
        )
        self.assertTrue(command.create_account)
        self.assertTrue(command.create_account.account_name == self.sample.sample_account_name)
        self.assertTrue(command.create_account.domain_id == self.sample.sample_domain_id)
        self.assertTrue(os.path.exists(self.sample.sample_keypair_path+".pub") and os.path.exists(self.sample.sample_keypair_path+".pri"))

    def test_no_account_name_command_generate(self):
        try:
            self.commands["CreateAccount"]["function"](
                {
                 "domain_id": self.sample.sample_domain_id
                 }
            )
        except CliException as e:
            self.assertTrue(e.args[0] == "account_name is required")
        else:
            self.fail("I want to exception")

    def test_not_str_account_name_command_generate(self):
        try:
            self.commands["CreateAccount"]["function"](
                {
                 "account_name": 1234,
                 "domain_id": self.sample.sample_domain_id
                 }
            )
        except CliException as e:
            self.assertTrue(e.args[0] == "account_name is <class 'str'>")
        else:
            self.fail("I want to exception")

    def test_not_str_keypair_command_generate(self):
        try:
            self.commands["CreateAccount"]["function"](
                {
                   "account_name": self.sample.sample_account_name,
                   "domain_id": self.sample.sample_domain_id,
                   "keypair_name": 1234
                 }
            )
        except CliException as e:
            self.assertTrue(e.args[0] == "keypair_name is <class 'str'>")
        else:
            self.fail("I want to exception")

if __name__ == "__main__":
    unittest.main()
